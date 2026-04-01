import sqlite3

conn = sqlite3.connect('example.sqlite3')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                rollno INTEGER UNIQUE, name TEXT NOT NULL, class TEXT )""")
cursor. executemany ("INSERT INTO student (rollno, name, class) VALUES (?,?,?)",
[(3,'Akhil','IXth'),(4,'Adithya',
                     'Xth'),(5,'Vinayak','IXth'),(6,'Nissam','IXth')])
conn.commit()
cls = 'IXth'
cursor.execute("""
SELECT *
FROM student
WHERE class=? AND rollno > ? AND name LIKE '%am'
""",(cls,3))

# starting 'john%'
# containing a word 'john%'
# ending 'john%'
data = cursor .fetchall()
print(data)

# print(data)
# conn. close()
# for row in data:
#     print(row[0])
#     print (row[1])
#     print (row[2])
#     print (row[3])