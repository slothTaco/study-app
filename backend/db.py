
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "flashcards.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_all_flashcards():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT question, answer FROM flashcards ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [{"question": row["question"], "answer": row["answer"]} for row in rows]

def insert_flashcard(question, answer):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO flashcards (question, answer) VALUES (?, ?)",
        (question, answer)
    )
    conn.commit()
    conn.close()

def delete_flashcard_by_index(index):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM flashcards ORDER BY id")
    rows = cur.fetchall()
    if 0 <= index < len(rows):
        cur.execute("DELETE FROM flashcards WHERE id = ?", (rows[index]["id"],))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False
