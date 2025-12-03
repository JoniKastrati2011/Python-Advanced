import sqlite3

from streamlit.cursor import Cursor

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY, 
    name TEXT
    )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY, 
    course_name TEXT,
    student_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
''')

cursor.execute("INSERT INTO students (name) Values('Alice')")
cursor.execute("INSERT INTO students (name) Values('Bob')")

cursor.execute("INSERT INTO courses (course_name, student_id) VALUES('Math', 1)")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES('Science', 1)")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES('Art', 2)")

connection.commit()

cursor.execute('''
SELECT students.name, courses.course_name
FROM students
JOIN courses ON students.student_id = courses.course_id
''')

rows = cursor.fetchall()
for row in rows:
    print(f"Student: {row[0]}, Course: {row[1]}")

connection.close()

