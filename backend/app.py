import os
import json
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'flashcards.json')

def load_flashcards():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return[]

def save_flashcards(flashcards):
    with open(DATA_FILE, 'w') as f:
        json.dump(flashcards, f, indent=2)

flashcards = load_flashcards()

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
    
    new_card = {
        "question": data["question"],
        "answer": data["answer"]
    }

    flashcards.append(new_card)
    save_flashcards(flashcards)

    return jsonify({"message": "Flashcard added"})

# Delete a flashcard
@app.route('/flashcards/<int:index>', methods=['DELETE'])
def delete_flashcard(index):
    if 0 <= index < len(flashcards):
        flashcards.pop(index)
        return jsonify({"message": "Flashcard deleted!"})
    return jsonify({"error": "Invalid index"}), 400

if __name__ == '__main__':
    app.run(debug=True)
