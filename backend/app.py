from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample flashcards
flashcards = [
    {"question": "What is Python?", "answer": "A programming language"},
    {"question": "What does Git do?", "answer": "Version control"}
]

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Get all flashcards
@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify(flashcards)

# Add a flashcard
@app.route('/flashcards', methods=['POST'])
def add_flashcard():
    data = request.get_json()
    flashcards.append({"question": data['question'], "answer": data['answer']})
    return jsonify({"message": "Flashcard added!", "flashcards": flashcards})

# Update a flashcard
@app.route('/flashcards/<int:index>', methods=['PUT'])
def update_flashcard(index):
    data = request.get_json()
    if 0 <= index < len(flashcards):
        flashcards[index] = {
            "question": data['question'],
            "answer": data['answer']
        }
        return jsonify({"message": "Flashcard updated", "flashcards": flashcards})
    return jsonify({"error": "Flashcard not found"}), 404

# Delete a flashcard
@app.route('/flashcards/<int:index>', methods=['DELETE'])
def delete_flashcard(index):
    if 0 <= index < len(flashcards):
        removed = flashcards.pop(index)
        return jsonify({"message": "Flashcard deleted!", "removed": removed})
    return jsonify({"error": "Invalid index"}), 400

if __name__ == '__main__':
    app.run(debug=True)
