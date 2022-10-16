from random import *

d = '~' * 15
database = { }


# The function to create an account
def register():
    print(f"\n\t\t{d} CREATE ACCOUNT {d}")
    first_name = input("First Name: ")
    lastname = input("Last Name: ")
    dob = input("Date-Of-Birth: ")
    email = input("Email: ")
    city = input("City: ")
    state = input("State: ")
    country = input("Country: ")
    password = input("Create Password: ")
    re_password = input("Retype Password: ")
    # to check if the password retyped is correct
    while password != re_password:
        re_password = input("Password does not match.\nRetype Password: ")
    # to generate a 10 digit random account number for user

    account_number = randrange(1111111111, 9999999999)
    pin = input("Create a 'Five' digit pin for transaction: ")
    # to check if the pin created is 5 digit
    while len(pin) < 5 or len(pin) > 5:
        print("Your pin is not of required standard")
        pin = input("Create a 'Five' digit pin for transaction: ")
    pin = int(pin)

    print(
        f"Hello {first_name} {lastname} you have successfully created an account with us."
        f"\nYour account number is {account_number}"
        f"\nYour account number would be required for all bank operations so Keep it safe.\n\n")

    # a serial num for identification in our data-base
    global serial_num
    serial_num = randrange(222222222222222, 999999999999999)
    database [serial_num] = [first_name, lastname, dob, email, city, state, country, password, re_password,
                             account_number, pin]
    # redirects to log in function
    log_in(database)


# The log in function
def log_in(database):
    print(f"\n\t\t{d} LOG-IN {d}")

    # receive email for log in
    login = input("Input your email: ")
    # check if eail is correct
    while login != (database [serial_num] [3]):
        print("Incorrect Email.\nTry again")
        login = input("Input Email: ")

    # receive password
    loginpassword = input("Input your password: ")
    # check if password is correct
    while loginpassword != (database [serial_num] [-3]):
        print("password is incorrect!")
        loginpassword = input("Input your password: ")
    bank_operations(database)


# The main banking startup page
def bank_startup():
    print(f"\n\t\t{d} ZIK-BANK {d}")
    acc_option = int(
        input("Welcome to this amazing mobile banking app.\n1.)Create account\n2.)Log in\n\tReply with 1 or 2 > "))
    if acc_option == 1:
        register()
    elif acc_option == 2:
        log_in(database)
    else:
        print("Invalid input")
        bank_startup()


# Bank operations
def bank_operations(database):
    print(f"Hello {database [serial_num] [0]} {database [serial_num] [1]} welcome to ZIK-BANK.\n ")
    operation = input(f"what would you like to do today:"
                      f"\n1.)Deposit\n2.)Withdraw\n3.)Check Account balance"
                      f"\n4.)Log-Out\n5.)Exit\n\tReply: ")
    operation = int(operation)
    if operation == 1:
        deposit()
    elif operation == 2:
        withdraw()
    elif operation == 3:
        details(database)
    elif operation == 4:
        log_in(database)
    elif operation == 5:
        exit()
    else:
        print("invalid option choosen")
        bank_operations(database)


def deposit():
    print(f"{d} Deposit {d}")


def withdraw():
    print(f"{d} Withdraw {d}")


def details(database):
    print(f"{d} Your Bank Account Details {d}")
    print(f"Name - {database [serial_num] [0]}-{database [serial_num] [1]}")
    print(f"Date Of Birth - {database [serial_num] [2]}")
    print(f"Email address - {database [serial_num] [3]}")
    print(f"Address - {database [serial_num] [4]},{database [serial_num] [5]},{database [serial_num] [6]}")
    print(f"Password - {database [serial_num] [7]}")
    print(f"Account Number - {database [serial_num] [9]}")
    print(f"Pin - *****")
    print()
    opt = input("would you like to check other bank operations 1.) Yes 2.) No : ")
    int(opt)
    if opt == 1:
        bank_operations(database)
    elif opt == 2:
        log_in(database)
    else:
        print("Invalid input")
        log_in(database)


# THE BANK MAIN CALL #
bank_startup()
