
import sqlite3
try:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Delete Dave's record
    cursor.execute('''
    delete from users
    where name = ?
    ''', ('abc',))

    conn.commit()

    if cursor.rowcount == 0:
        print("Abc not found. No record deleted.")
    else:
        print("Abc's record deleted successfully.")

except sqlite3.Error as e:
    print("An error occurred while deleting data:", e)

finally:
    if conn:
        conn.close()
