from database import save_sent_articles, init_db, is_duplicate

init_db()
save_sent_articles("https://example.com/fake-article", "Fake Title", "2026-08-13")

import sqlite3

connection = sqlite3.connect("Briefly.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM sent_articles")
print(cursor.fetchall())
connection.close()