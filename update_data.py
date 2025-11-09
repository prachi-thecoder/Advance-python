import sqlite3
try:
    conn=sqlite3.connect('student_marks.db')
    cursor = conn.cursor()

    cursor.execute('''update student_marks
                   set marks = ?
                   where name = ?''',(77,"prachu"))
    conn.commit()
    rows = cursor.fetchall()
    print("row count",cursor.rowcount)
    if(cursor.rowcount == 0):
        print("marks not found")
    else:
        print("marks are updated")
        cursor.execute('select * from student_marks where marks = ?',(77,))
        updated_row = cursor.fetchone()
        print("updated row",updated_row)

except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()

# write a prog to accept user id and new password from user and change old pass to new pass 
import sqlite3
try:
    conn=sqlite3.connect('users.db')
    cursor = conn.cursor()
    # a=input("enter a id:"
    b=input("enter a id:")
    c=input("enter a password:")
    cursor.execute('''update users
                   set userpassword= ?
                   where  id = ?''',((c,b)))
    conn.commit()
    rows = cursor.fetchall()
    print("row count",cursor.rowcount)
    if(cursor.rowcount == 0):
        print("password is not found")
    else:
        print("password is updated")
        cursor.execute('select * from users where name = ?',("pqr",))
        updated_row = cursor.fetchone()
        print("updated row",updated_row)

except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:  
        conn.close()

