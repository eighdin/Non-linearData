import sqlite3

# Create student.db if it does not exist, otherwise connect
conn = sqlite3.connect('student.db')
# Create a cursor for the connection to execute commands
cursor = conn.cursor()

# cursor.execute(
#     "CREATE TABLE student_info (firstName TEXT, lastName TEXT, email TEXT, dob TEXT,"
#     "isCyber TEXT, isDS TEXT, gender TEXT)"
# )
cursor.execute("INSERT INTO student_info VALUES ('David', 'M', 'davidm@mercyhurst.edu', '03/12/2000', '1', '0', '1')")
conn.commit() # commit all the changes that were made to the DB
conn.close() # close connection to DB
