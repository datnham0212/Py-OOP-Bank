import main 
import bankAccount
while(True):
    print("---------------------------------")
    print("  Welcome to the Bank of Python  ")
    print("---------------------------------")
    print("1. Login")
    print("2. Sign up")
    print("0. Exit")
    print("---------------------------------")
    choice = int(input())

    if (choice == 1):
        print("--------------Login--------------")
        id = input("Account ID: ")
        pwd = input("Password: ")
        print("---------------------------------")

        if(id == "root" and pwd == "root"):
            main.main()
        else:
            print("Invalid account ID or password, please try again!")
            continue

    elif (choice == 2):
        print("--------------Sign up--------------")
        input("Name: ")
        input("Password: ")
        print("---------------------------------")

        print("Your account ID will be: ??????")
        print("0. Go back")
        if (int(input()) == 0):
            continue

    elif (choice == 0):
        break