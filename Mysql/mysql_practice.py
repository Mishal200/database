import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password=""
)


cursor = conn.cursor()

# creates a database
cursor.execute("CREATE DATABASE IF NOT EXISTS syn_college")

# specifies the database
cursor.execute("USE syn_college")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
age INT,
department VARCHAR(20)

""")

cursor.execute("INSERT INTO students (name, age, department) VALUES (%s,%s,%s)",('Saurav',19,'CS'))
conn.commit()

print(cursor.rowcount, "records inserted")

cursor.close()
conn.close()