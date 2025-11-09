import sqlite3
try:
    # Connect to the database (or create it)
    conn = sqlite3.connect('students.db')       #create a file 
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    create table if not exists students (
        id integer primary key autoincrement,
        name text not null,
        age integer,
        marks real
    )
    ''')
    print("Table created successfully.")

    # Save changes
    conn.commit()

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    # Close the connection safely
    if conn:
        conn.close()

# 2nd program
import sqlite3
try:
    con=sqlite3.connect("user.db")
    cursor = con.cursor()
    cursor.execute('''
    create table if not exists user(
                name text,
                mobileno text,
                id integer,
                password text,
                emailid text

                )
    ''')
    print("created table ")
    con.commit()
except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    # Close the connection safely
    if con:
        con.close()