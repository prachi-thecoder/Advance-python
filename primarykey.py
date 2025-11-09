import sqlite3
try:
    conn = sqlite3.Connection("primary.db")
    cursor = conn.cursor()
    # cursor.execute('''
    #                create table if not exists pr(
    #                         id integer primary key autoincrement,
    #                         name text )''')
    # print("yes table is created ")
    # conn.commit()
    cursor.execute('''
insert into pr(id,name)
                   values(?,?)''',(1,"prq",))
    print("done your data is inserted successfully ")
    conn.commit()
except sqlite3.Error as e:
    print("error",e)
finally:
    if conn:
        conn.close()
# 
