import sqlite3

conn = sqlite3.connect('example.sqlite3')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                rollno INTEGER UNIQUE, name TEXT NOT NULL, class TEXT )""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rollno INTEGER,
    subject TEXT,
    mark INTEGER,
    FOREIGN KEY (rollno) REFERENCES student(rollno)
    )
""")


cursor.executemany("INSERT INTO marks(rollno,subject,mark) values(?,?,?)", [
    (1,'Maths',50),
    (1,'English',55),
    (1,'Science',81),
    (2,'Maths',50),
    (2,'English',55),
    (2,'Science',83),
    (3,'Maths',60),
    (3,'English',75),
    (3,'Science',81)
])


conn.commit()


cursor.execute("""
SELECT student.rollno,student.name,marks.mark,marks.subject
FROM student
JOIN marks ON student.rollno = marks.rollno
""")

cursor.execute("SELECT * FROM marks")


data = cursor.fetchall()
print(data)


conn.close()