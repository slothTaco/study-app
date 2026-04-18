<<<<<<< HEAD
# Study App (Flask)

A simple, lightweight **study and flashcard application** built with **Flask** and **vanilla JavaScript**.

This project was created as a learning and portfolio project to better understand how backend APIs, frontend state, and persistent data storage work together in a real application.

---

## 🚀 Features

- Create flashcards with a **question**, **answer**, and optional **topic**
- Persistent storage using a local JSON file
- Topic-based filtering to focus revision on specific subjects
- Randomized review mode to encourage active recall
- Click-to-reveal answers for self-testing
- Clean, minimal UI with no external frontend frameworks

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Data Storage:** JSON file
- **Environment:** Python virtual environment

---

## 🤔 Why Flask?

Study App (Flask)

A simple, lightweight study and flashcard application built with Flask and vanilla JavaScript.

This project was created as a learning and portfolio project to better understand how backend APIs, frontend state, and persistent data storage work together in a real application.
🚀 Features

    Create flashcards with a question, answer, and optional topic
    Persistent storage using a local JSON file
    Topic-based filtering to focus revision on specific subjects
    Randomized review mode to encourage active recall
    Click-to-reveal answers for self-testing
    Clean, minimal UI with no external frontend frameworks

🛠️ Tech Stack

    Backend: Python, Flask
    Frontend: HTML, CSS, JavaScript
    Data Storage: JSON file
    Environment: Python virtual environment

🤔 Why Flask?
)

Flask was chosen because it is lightweight and flexible, making it ideal for learning how web applications work at a lower level without unnecessary abstraction.

This allowed me to focus on:
<<<<<<< HEAD
 Routing and APIs
 Handling HTTP requests
 Managing application state
 Debugging real-world edge cases

---

## ⚙️ How It Works

 Flashcards are stored on the backend and exposed through REST-style routes
 The frontend uses `fetch()` to interact with the API dynamically
 Topics are generated automatically based on existing flashcards
 The UI always reflects the current state of the underlying data

---

## ▶️ Running the App Locally

```bash
=======

    Routing and APIs
    Handling HTTP requests
    Managing application state
    Debugging real-world edge cases

⚙️ How It Works

    Flashcards are stored on the back-end and exposed through REST-style routes
    The front-end uses fetch() to interact with the API dynamically
    Topics are generated automatically based on existing flashcards
    The UI always reflects the current state of the underlying data

▶️ Running the App Locally

 (Document AWS EC2 deployment process)
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask

# Run the application
python app.py
 HEAD
=======


## Deployment (AWS EC2)

This application was deployed to AWS EC2 using an Ubuntu 24.04 LTS instance.

The deployment was done manually to better understand how a Python web
application runs outside of a local development environment.

Key steps included:
- Provisioning an EC2 instance (t3.micro)
- Configuring security groups for SSH and application access
- Connecting via SSH using key-based authentication
- Creating and activating a Python virtual environment
- Installing dependencies via requirements.txt
- Running the Flask backend on a public IP

The instance is stopped when not in use to remain within AWS Free Tier credits.


