import sqlite3
from customer_points import Customer
conn = sqlite3.connect('customer_points.db')
c = conn.cursor()
def returning_email(email):
    email = ''
    while  "@" not in  email:
        print("Please enter email.")
        email = input()
    return email
    
def add_customer_points(customer_points, is_existing):
    if is_existing:
        customer_points += 50
    else:
        customer_points += 10

def first_name(f_name):
    f_name=''
    if f_name.isnumeric():
         print("Letters only.Do not use numbers")
    elif():
        return f_name
    
def last_name(l_name):
    l_name = ''
    if l_name.isnumeric():
       print("Letters only.Do not use numbers.") 
    elif():
        return l_name
    
def enter_store():
    print("Welcome to Dusty Mart.")
    store = input("Are you a returning customer? Y/N?:").lower()
    if store == "y":
        email = returning_email(input("Excellent! Please enter your email"))
    if store == "n":
        print("No worrries! Let's get you set up.")
        fname = first_name(input("Please enter your first name."))
        lname = last_name(input("Please enter your last name."))
        email = enter_email(input("Excellent! Please enter your email"))

    
    
    

        c.execute("INSERT INTO customers VALUES(?, ?, ?, ?)", (fname, lname, 10, email))    
    
#allows to excute some sql commands

#create customer table that holds first, name,last name, and points
#c for the cursor we've created
#c.execute("""CREATE TABLE customer(
#                   first text,
#                  last text,
#                 points integer
 #                  )""")
#commits current transaction and changes
#c.execute("INSERT INTO customers VALUES('Horatio', 'Caine', 456)")
#c.execute("INSERT INTO customers VALUES('Dave', 'Folkson', 58600)")
#c.execute("INSERT INTO customers VALUES('Callie', 'Dusquene', 78)")
#c.execute("INSERT INTO customers VALUES('Kimberly', 'Vaughn', 100)")
#c.execute("INSERT INTO customers VALUES('Luke', 'Dennison', 325)")
#conn.commit()
#c.execute("SELECT * FROM customers")
#print(c.fetchall())
 
enter_store()
conn.commit()
conn.close()
