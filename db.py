import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12774662",
        password="vgqK48Qsl6",
        database="sql12774662"
    )

def fetch_user():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, image FROM user LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result

def update_user(name, phone, image):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user")  # Only one user allowed
    cursor.execute("INSERT INTO user (name, phone, image) VALUES (%s, %s, %s)", (name, phone, image))
    conn.commit()
    conn.close()
