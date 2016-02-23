import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
    c.execute('INSERT INTO posts VALUES("X", "I\'m X")')
    c.execute('INSERT INTO posts VALUES("Genius", "I\'m the best")')
