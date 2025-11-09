'''Create (Insert Record) Ask the user for customer_name, item, quantity, and price. Insert a new order into the
 orders table. Read (View Records) Display all orders with proper formatting (order ID, name, item, total price).
Update (Modify Record) Update the quantity or price of an existing order using its order_id. Delete (Remove Record)
Delete an order by order_id.'''

import sqlite3
try:
    con = sqlite3.connect('program.db')
    cursor = con.cursor()
    cursor.execute('''
                    create table if not exists program(
                    customer_name text,
                    order_id integer,
                    item text,
                    price integer,
                   quantity integer
                   )
''')
    print("table successfully created")

#   insert data 

    con.commit()
    p=input("enter a customer name :")
    r=int(input("enter a order id:"))
    o=input("enter a item:")
    g=int(input("enter a price:"))
    ra=int(input("enter a quantity:"))
    cursor.execute('''
                   insert  into program(customer_name,item,price,quantity,order_id)
                   values (?,?,?,?,?)''',(p,r,o,g,ra)) 
    con.commit()
    print("")

    print("enter for 2nd person.")
    p=input("enter a customer name :")
    r=int(input("enter a order id:"))
    o=input("enter a item:")
    g=int(input("enter a price:"))
    ra=int(input("enter a quantity:"))
    cursor.execute('''
                   insert  into program(customer_name,item,price,quantity,order_id)
                   values (?,?,?,?,?)''',(p,r,o,g,ra))
    
    print("data insertd successfully")
    con.commit()
    print("")

# display data

    cursor.execute('select * from program')
    print("data record is:")
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row=cursor.fetchone()
    con.commit() 
    print("")

# update quantity

    b=input("enter a id:")
    z=input("enter a new quantity:")
    cursor.execute('''
              update program
              set quantity = ?
              where order_id = ?
  ''',(z,b))
    row = cursor.fetchall()
    print("data update successfully.")
    con.commit()
    print("")

# data delete

    delete=input("enter a order id to delete order:")
    cursor.execute(''' 
                    delete from program
                    where order_id = ? ''',delete)
    print("data delete successfully")
    con.commit()
    print("")
except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    if con:
        con.close()  