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

