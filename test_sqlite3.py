import sqlite3

conn = sqlite3.connect("test_database.db")
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO users(name) VALUES ("Keerthana")')
cursor.execute('INSERT INTO users(name) VALUES ("Sree")')
conn.commit()

cursor.execute('SELECT * FROM users')
print(cursor.fetchall())

conn.close()