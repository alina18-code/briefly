import sqlite3


def init_db():
    connection = sqlite3.connect("Briefly.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sent_articles (
        id INTEGER PRIMARY KEY,
        link TEXT UNIQUE,
        title TEXT,
        date_sent TEXT
    )""")
    connection.commit()
    connection.close()


if __name__ == "__main__":
    init_db()