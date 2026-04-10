from models.db import cursor, conn

def add_user(username, password):
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
