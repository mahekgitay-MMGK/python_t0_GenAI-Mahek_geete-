


"""SQL theory: Structured Query Language (SQL) is used to manage data in
relational databases. Data is stored in tables made up of rows and columns.

This example uses SQLite, a lightweight database stored in a local file.
CREATE TABLE defines a table, INSERT adds records, and SELECT retrieves
records. WHERE filters results, while ORDER BY sorts them. COMMIT saves
database changes, and DROP TABLE removes a table.
"""

import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("CREATE TABLE students (id INTEGER , name TEXT, marks INTEGER)")
cursor.execute("INSERT INTO students VALUES (1,'Mahek', 90),(2,'Aarav', 85),(3,'Riya', 95),(4,'Aditya', 80),(5,'Ananya', 88)")

print("Topper >70:")
cursor.execute("SELECT * FROM students WHERE marks > 70 ORDER BY marks DESC")
print(cursor.fetchall())

print("find riya:")
cursor.execute("SELECT * FROM students WHERE name = 'Riya'")
print(cursor.fetchall())

conn.commit()
conn.close()
     
print("SQL operations completed successfully.")