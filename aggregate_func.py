# count function count the no of rows
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select count(*) from student_marks')
    rows = cursor.fetchall()

    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()

# 
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select marks,count(marks) from student_marks where marks = ? or marks = ?',(95,99,))

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()

# sum function
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select sum(marks) from student_marks')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
# avg func
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select avg(marks) from student_marks')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
# min fun
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select min(marks) from student_marks')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
#max fun 
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select max(marks) from student_marks')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
   
     conn.close()

# upper fun 
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select upper(name) from student_marks')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()

# lower fun 
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select lower(name) from student_marks')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
# order by 
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select * from student_marks order by id ')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
# descending order
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select * from student_marks order by id desc ')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()

#  ascending by name by limit
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select * from student_marks order by name limit 3')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
        
# multiple column
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select * from student_marks order by id ,marks')

    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()

#group by 
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    cursor.execute('select name,max(marks) from student_marks group by name')
    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
# 
import sqlite3
try:
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()
    # cursor.execute('alter table student_marks add column city text')
    # conn.commit()
    cursor.execute('''insert into students 
                    values(?,?,?)''',(1,'kkq',33))
    conn.commit()
    # cursor.execute('select name from students group by city order by name desc ')
    rows = cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
# 
