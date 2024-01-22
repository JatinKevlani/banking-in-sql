from functions import *
import os
import time

def main(database_connection):
    choice = True
    while choice:
        os.system("cls")
        menu()
        choice = int(input("Enter your choice : "))
        if choice == 0:
            print("Bye!!!")
            pressEnterToContinue(exit = True)

        if choice == 1:
            addCustomer(database_connection)
            pressEnterToContinue()

        elif choice == 2:
            myresult = searchCustomer(database_connection)
            if len(myresult) == 0:
                print("Customer not found!")
            else:
                for result in myresult:
                    print(result)
                    print()
            pressEnterToContinue()

        elif choice == 3:
            id = int(input("Enter ID to search information : "))
            myresult = searchCustomer(database_connection, id)
            if len(myresult) == 0:
                print("Customer not found!")
            else:
                print(myresult)
            pressEnterToContinue()

        elif choice == 4:
            id = int(input("Enter ID in which you want to deposit money : "))
            myresult = searchCustomer(database_connection, id)
            if len(myresult) == 0:
                print("Customer not found!")
            else:
                amount = int(input("Enter the amount you want to deposit : "))
                deposit(database_connection, id, amount)
                print(f"Rs.{amount} deposited successfully!")
                print(f"Your updated balance is {myresult[0][-1] + amount}.")
            pressEnterToContinue()

        elif choice == 5:
            id = int(input("Enter ID from which you want to withdraw money : "))
            myresult = searchCustomer(database_connection, id)
            if len(myresult) == 0:
                print("Customer not found!")
            else:
                amount = int(input("Enter the amount you want to withdraw : "))
                if amount > myresult[0][-1]:
                    print("Cannot withdraw money more than current balance!")
                    print(f"Your current balance is : Rs.{myresult[0][-1]}")
                else:
                    withdraw(database_connection, id, amount)
                    print(f"Rs.{amount} withdrawn successfully!")
                    print(f"Your updated balance is {myresult[0][-1] - amount}.")
            pressEnterToContinue()

        elif choice == 6:
            receiver = int(input("Enter ID in which you want to transfer money : "))
            myresult = searchCustomer(database_connection, receiver)
            if len(myresult) == 0:
                print("Receiver not found!")
            else:
                sender = int(input("Enter ID from which you want to transfer money : "))
                myresult = searchCustomer(database_connection, sender)
                if len(myresult) == 0:
                    print("Sender not found!")
                else:
                    amount = int(input("Enter the amount you want to transfer : "))
                    if amount > myresult[0][-1]:
                        print("Cannot transfer money more than current balance!")
                        print(f"Your current balance is : Rs.{myresult[0][-1]}")
                    else:
                        deposit(database_connection, receiver, amount)
                        withdraw(database_connection, sender, amount)
                        print("Money transferred successfully!")
            pressEnterToContinue()

        else:
            print("Invalid Choice!\nPlease enter a valid option.")
            pressEnterToContinue()

if __name__ == "__main__":
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port = 3307,
            user="root",
            password="system",
            database="projects"
        )
        if mydb.is_connected():
            print("Connecting to the server...")
            time.sleep(1.5)
            print("Connection successfull!")
            print("Opening application...")
            time.sleep(2)
        else:
            print("Connection failed!")
    except mysql.connector.Error as e:
        print("Connecting to the server...")
        time.sleep(3)
        print("Server is not responding...")
        time.sleep(1)
        print("Kindly check your connection.")
        pressEnterToContinue(exit = True)
        response = input()
        if response == "r":
            print("Error:", e)
        exit()
    
    main(mydb)