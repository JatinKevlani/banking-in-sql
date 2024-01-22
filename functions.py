import mysql.connector

def pressEnterToContinue(exit = False):
    if exit == True:
        print("Press ENTER to exit...", end="")
    else:   
        print("Press ENTER to continue...", end="")
    input()

def menu():
    print("Enter 0 to exit.")
    print("Enter 1 to add new customer.")
    print("Enter 2 to get information all customers.")
    print("Enter 3 to get information of particular customer.")
    print("Enter 4 to deposit money.")
    print("Enter 5 to withdraw money.")
    print("Enter 6 to transfer money.")

def addCustomer(database_connection):
    try:
        cursor = database_connection.cursor()

        id = int(input("Enter customer ID : "))
        name = input("Enter customer name : ")
        balance = int(input("Enter initial deposit amount : "))

        cursor.execute(f"INSERT INTO bank VALUES ({id}, '{name}', {balance})")
        database_connection.commit()

        print("Customer added successfully!")
    except mysql.connector.Error as e:
        print("Error:", e)

def searchCustomer(database_connection, id = 0):
    mycursor = database_connection.cursor()
    if id == 0:
        mycursor.execute("SELECT * FROM bank")
    else:
        mycursor.execute(f"SELECT * FROM bank WHERE id = {id}")

    myresult = mycursor.fetchall()

    return myresult

def deposit(database_connection, id, amount):
    mycursor = database_connection.cursor()
    mycursor.execute(f"UPDATE bank SET balance = balance + {amount} WHERE id = {id}")
    database_connection.commit()

def withdraw(database_connection, id, amount):
    mycursor = database_connection.cursor()
    mycursor.execute(f"UPDATE bank SET balance = balance - {amount} WHERE id = {id}")
    database_connection.commit()