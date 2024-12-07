import sqlite3

# Create student.db if it does not exist, otherwise connect
conn = sqlite3.connect('student_id.db')
# Create a cursor for the connection to execute commands
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS student_id (firstName TEXT, lastName TEXT, id TEXT)")
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
id = input("Enter the student ID: ")
insert_command = f'INSERT INTO student_id VALUES ("{first_name}", "{last_name}", "{id}")'

cursor.execute(insert_command)
conn.commit() # commit all the changes that were made to the DB
conn.close() # close connection to DB
