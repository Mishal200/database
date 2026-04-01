import sqlite3


conn = sqlite3.connect("school.db")
cursor = conn.cursor()



cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rollno INTEGER UNIQUE NOT NULL,
    class TEXT NOT NULL,
    section TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rollno INTEGER,
    subject TEXT NOT NULL,
    mark INTEGER NOT NULL,
    FOREIGN KEY (rollno) REFERENCES students(rollno)
)
""")

try:
    cursor.executemany("""
    INSERT INTO students (name, rollno, class, section)
    VALUES (?, ?, ?, ?)
    """, [
        ("John", 101, "10", "A"),
        ("Mary", 102, "10", "B"),
        ("Alex", 103, "10", "A")
    ])
    cursor.executemany("""
    INSERT INTO marks (rollno, subject, mark)
    VALUES (?, ?, ?)
    """, [
        (101, "Maths", 85),
        (101, "Science", 78),
        (102, "Maths", 90),
        (103, "Science", 60)
    ])
    conn.commit()
except:
    pass 

def add_student():
    name = input("Name: ")
    rollno = int(input("Rollno: "))
    cls = input("Class: ")
    section = input("Section: ")
    try:
        cursor.execute("INSERT INTO students (name, rollno, class, section) VALUES (?, ?, ?, ?)",
                       (name, rollno, cls, section))
        conn.commit()
        print("Student added successfully!")
    except:
        print("Error: Rollno already exists.")

def add_marks():
    rollno = int(input("Rollno: "))
    subject = input("Subject: ")
    mark = int(input("Mark: "))
    cursor.execute("INSERT INTO marks (rollno, subject, mark) VALUES (?, ?, ?)", (rollno, subject, mark))
    conn.commit()
    print("Marks added successfully!")

# --- READ --- #
def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def view_marks():
    cursor.execute("SELECT * FROM marks")
    for row in cursor.fetchall():
        print(row)

def view_marks_by_student():
    rollno = int(input("Enter Rollno: "))
    cursor.execute("SELECT * FROM marks WHERE rollno=?", (rollno,))
    for row in cursor.fetchall():
        print(row)

def view_students_with_marks():
    cursor.execute("""
    SELECT s.rollno, s.name, s.class, s.section, m.subject, m.mark
    FROM students s
    JOIN marks m ON s.rollno = m.rollno
    """)
    for row in cursor.fetchall():
        print(row)

def view_marks_by_subject():
    subject = input("Enter Subject: ")
    cursor.execute("SELECT * FROM marks WHERE subject=?", (subject,))
    for row in cursor.fetchall():
        print(row)

def view_students_sorted():
    cursor.execute("SELECT * FROM students ORDER BY name")
    for row in cursor.fetchall():
        print(row)

def view_highest_mark():
    cursor.execute("SELECT MAX(mark) FROM marks")
    print("Highest Mark:", cursor.fetchone()[0])

def view_lowest_mark():
    cursor.execute("SELECT MIN(mark) FROM marks")
    print("Lowest Mark:", cursor.fetchone()[0])

def view_average_marks_per_student():
    cursor.execute("""
    SELECT rollno, AVG(mark) FROM marks GROUP BY rollno
    """)
    for row in cursor.fetchall():
        print("Rollno:", row[0], "Average:", row[1])

def view_total_marks_per_student():
    cursor.execute("""
    SELECT rollno, SUM(mark) FROM marks GROUP BY rollno
    """)
    for row in cursor.fetchall():
        print("Rollno:", row[0], "Total:", row[1])

def view_students_above_80():
    cursor.execute("SELECT * FROM marks WHERE mark>80")
    for row in cursor.fetchall():
        print(row)

def view_subjectwise_average():
    cursor.execute("SELECT subject, AVG(mark) FROM marks GROUP BY subject")
    for row in cursor.fetchall():
        print(row)

def view_failed_students():
    cursor.execute("SELECT * FROM marks WHERE mark<40")
    for row in cursor.fetchall():
        print(row)

def view_top_3_students():
    cursor.execute("""
    SELECT rollno, SUM(mark) as total
    FROM marks
    GROUP BY rollno
    ORDER BY total DESC
    LIMIT 3
    """)
    for row in cursor.fetchall():
        print(row)

# --- UPDATE --- #
def update_student():
    rollno = int(input("Enter Rollno to update: "))
    name = input("Enter new name: ")
    cls = input("Enter new class: ")
    section = input("Enter new section: ")
    cursor.execute("UPDATE students SET name=?, class=?, section=? WHERE rollno=?", (name, cls, section, rollno))
    conn.commit()
    print("Student updated!")

def update_marks():
    rollno = int(input("Rollno: "))
    subject = input("Subject: ")
    new_mark = int(input("New Mark: "))
    cursor.execute("UPDATE marks SET mark=? WHERE rollno=? AND subject=?", (new_mark, rollno, subject))
    conn.commit()
    print("Marks updated!")

def update_subject_name():
    old_subject = input("Old Subject Name: ")
    new_subject = input("New Subject Name: ")
    cursor.execute("UPDATE marks SET subject=? WHERE subject=?", (new_subject, old_subject))
    conn.commit()
    print("Subject name updated!")

# --- DELETE --- #
def delete_student():
    rollno = int(input("Rollno: "))
    cursor.execute("DELETE FROM students WHERE rollno=?", (rollno,))
    conn.commit()
    print("Student deleted!")

def delete_marks():
    rollno = int(input("Rollno: "))
    cursor.execute("DELETE FROM marks WHERE rollno=?", (rollno,))
    conn.commit()
    print("Marks deleted!")

def delete_marks_by_subject():
    subject = input("Subject: ")
    cursor.execute("DELETE FROM marks WHERE subject=?", (subject,))
    conn.commit()
    print("Marks of subject deleted!")

# ------------------- Menu ------------------- #
menu = {
    "1": add_student,
    "2": add_marks,
    "3": view_students,
    "4": view_marks,
    "5": view_marks_by_student,
    "6": view_students_with_marks,
    "7": view_marks_by_subject,
    "8": view_students_sorted,
    "9": view_highest_mark,
    "10": view_lowest_mark,
    "11": view_average_marks_per_student,
    "12": view_total_marks_per_student,
    "13": view_students_above_80,
    "14": view_subjectwise_average,
    "15": view_failed_students,
    "16": view_top_3_students,
    "17": update_student,
    "18": update_marks,
    "19": update_subject_name,
    "20": delete_student,
    "21": delete_marks,
    "22": delete_marks_by_subject,
    "23": exit
}

while True:
    print("\n--- Student Marks Management ---")
    print("1. Add Student\n2. Add Marks\n3. View Students\n4. View Marks\n5. View Marks by Student")
    print("6. View Students with Marks\n7. View Marks by Subject\n8. View Students Sorted\n9. Highest Mark")
    print("10. Lowest Mark\n11. Average Marks per Student\n12. Total Marks per Student\n13. Students >80")
    print("14. Subject Wise Average\n15. Failed Students\n16. Top 3 Students\n17. Update Student\n18. Update Marks")
    print("19. Update Subject Name\n20. Delete Student\n21. Delete Marks\n22. Delete Marks by Subject\n23. Exit")

    choice = input("Enter choice: ")
    try:
        menu[choice]()
    except:
        print("Invalid choice!")