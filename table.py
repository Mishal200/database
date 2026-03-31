import sqlite3

conn = sqlite3.connect('example.sqlite3')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rollno INTEGER UNIQUE,
    name TEXT NOT NULL,
    class TEXT
)
""")

cursor.executemany(
    "INSERT OR IGNORE INTO student (rollno, name, class) VALUES (?, ?, ?)",
    [(3, 'Akhil', 'IXth'),
     (4, 'Adithya', 'Xth'),
     (5, 'Vinayak', 'IXth'),
     (6, 'Nissam', 'IXth')]
)

conn.commit()