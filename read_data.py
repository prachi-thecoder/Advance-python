import sqlite3
try:
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('select * from students')
    row = cursor.fetchall()
    print("row count",cursor.rowcount)
    print("student records:")
    for row in row:
        print("id:",row[0])
        print('name:',row[1])
        print('marks:',row[3])
        print("")
except sqlite3.Error as e:
    print("an error occured while fetching data",e)

finally:
    if conn:
        conn.close()
        
#reading data from users.db file
import sqlite3
try:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('select * from users')
    print("row count",cursor.rowcount)
    print("student records:")
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row=cursor.fetchone()
    # for row in row:
    #     print("id:",row[0])
    #     print('name:',row[1])
    #     print('marks:',row[3])
    #     print("")
    
except sqlite3.Error as e:
    print("an error occured while fetching data",e)

finally:
    if conn:
        conn.close() 

# reading data from student_marks file
import sqlite3
try:
    conn = sqlite3.connect('student_marks.db')
    cursor = conn.cursor()

    cursor.execute('select * from student_marks')
   
    print("row count",cursor.rowcount)
    print("student records:")
    row = cursor.fetchmany(2)
    while row:
        for row in row:
            print(row)
        row=cursor.fetchmany(2)
    # for row in row:
    #     print("id:",row[0])
    #     print('name:',row[1])
    #     print('marks:',row[3])
    #     print("")
    
except sqlite3.Error as e:
    print("an error occured while fetching data",e)

finally:
    if conn:
        conn.close() 