import sqlite3

# try:
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#         insert into students (id,name,age,marks)
#         values (?, ?, ?, ?)
#         ''',(1,"Diksha",18,80))
#     conn.commit()
    
#     print("Records are inserted successfully.")

# except sqlite3.Error as e:
#     print("An error occured while inserting data:",e)
# finally:
#     if conn:
#         cursor.close()
#         conn.close()
try:
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    students=[
        (1,'abc',20,85.5),
        (2,'pqr',22,78.0),
        (3,'asd',19,92.3)
    ]
    for student in students:
        # cursor.execute('''
        #     insert into students (id,name,age,marks)
        #     values (?, ?, ?, ?)
        #     ''',student)
        print("no of rows in table",cursor.rowcount)
        conn.commit()
    
    print("Records are inserted successfully.")

except sqlite3.Error as e:
    print("An error occured while inserting data:",e)

finally:
    if conn:
        cursor.close()
        conn.close()

# to insert data in user table and print all data from user tablle
import sqlite3
try:
    # Connect to the database (or create it)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    create table if not exists users (
        id integer,
        name text,
        userpassword text,
        useremail text
    )
    ''')

    print("Table created successfully.")

    # Save changes
    conn.commit()
    # cursor = conn.cursor()
    users=(1,'abc','prachii','abc@gmail')

    users=(2,'pqr','prachu','pqr@gmail')
    
    cursor.execute('''insert into users (id,name,userpassword,useremail)
             values (?, ?, ?, ?)
             ''',users)
    conn.commit()
except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    if conn:
        conn.close()

# create a table of student_marks and insert data as id name marks
import sqlite3
try:
    con = sqlite3.connect('student_marks.db')
    cursor = con.cursor()

    cursor.execute('''create table if not exists students(
                    id integer primary key autoincrement,
                    name text,
                    marks integer)
                    ''')
    print("tale created successfully")
    con.commit()
    student_marks=(1,"sanchi",95)
    cursor.execute('''insert into student_marks (id,name,marks)
                   values (?,?,?)''',student_marks)
    con.commit()
    student_marks=(2,"prachu",97)
    cursor.execute('''insert into student_marks (id,name,marks)
                   values (?,?,?)
                   ''',student_marks)
    con.commit()
    student_marks=(3,"prachi",100)
    cursor.execute('''insert into student_marks (id,name,marks)
                   values (?,?,?)
                   ''',student_marks)
    con.commit()
except sqlite3.Error as e:
    print("An error occurred:", e)
finally:
    if con:
        con.close()

