# Study App (Flask)

A simple, lightweight flashcard study application built with Flask and vanilla JavaScript.

This project was created as a learning and portfolio project to better understand how backend APIs, frontend state, and persistent data storage work together in a real, deployed application.

---

## 🚀 Features

- Create flashcards with a question, answer, and optional topic
- Persistent storage using a SQLite database
- Topic-based organisation for focused revision
- Randomised review mode to encourage active recall
- Click-to-reveal answers for self-testing
- Clean, minimal UI with no external frontend frameworks

---

## 🛠️ Tech Stack

**Backend**
- Python
- Flask

**Frontend**
- HTML
- CSS
- Vanilla JavaScript

**Data Storage**
- SQLite (file-based, server-side persistence)

**Runtime / Deployment**
- Gunicorn (WSGI server)
- systemd (process supervision)
- AWS EC2 (Ubuntu 24.04 LTS)

---

## 🤔 Why Flask?

Flask was chosen because it is lightweight and flexible, making it ideal for learning how web applications work without heavy abstraction.

This allowed me to focus on:
- Routing and APIs
- Handling HTTP requests
- Managing application state
- Debugging real-world edge cases
- Understanding how applications behave once deployed

---

## ⚙️ How It Works

- Flashcards are stored on the backend and exposed through REST-style API routes
- The frontend uses `fetch()` to interact with the API dynamically
- Application state is managed server-side
- Data persists across restarts via a SQLite database
- Gunicorn runs the app as a multi-process service
- systemd ensures the app starts on boot and restarts if it crashes

---

## ▶️ Running the App Locally

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
