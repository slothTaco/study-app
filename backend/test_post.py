import requests

new_card = {"question": "What is Flask?", "answer": "A Python web framework"}
response = requests.post("http://127.0.0.1:5000/flashcards", json=new_card)
print(response.json())