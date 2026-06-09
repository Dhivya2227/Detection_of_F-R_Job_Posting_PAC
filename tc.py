import sqlite3

conn = sqlite3.connect("truehire.db")

cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()

print("Database created successfully!")