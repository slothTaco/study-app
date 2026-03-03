from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample flashcards
flashcards = [
    {"question": "What is Python?", "answer": "A programming language"},
    {"question": "What does Git do?", "answer": "Version control"}
]

@app.route('/')
def home():
    return "Welcome to Study App API!"

@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify(flashcards)

@app.route('/flashcards', methods=['POST'])
def add_flashcard():
    data = request.get_json()  # Read JSON data sent by frontend
    flashcards.append({"question": data['question'], "answer": data['answer']})
    return jsonify({"message": "Flashcard added!", "flashcards": flashcards})
if __name__ == '__main__':
    app.run(debug=True)