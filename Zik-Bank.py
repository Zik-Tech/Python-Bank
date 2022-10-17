from random import *

d = '~' * 15
database = { }
acc_balance = 0
prompt = "This field is reqired"


# The function to create an account
def register(database):
    print(f"\n\t\t{d} CREATE ACCOUNT {d}")
    first_name = input("First Name: ")
    # to ensure that this field is not empty
    while len(first_name) <= 1:
        print(prompt)
        first_name = input("First Name: ")
    # to ensure that this field is not empty
    lastname = input("Last Name: ")
    while len(lastname) <= 1:
        print(prompt)
        lastname = input("Last Name: ")
    # to ensure that this field is not empty
    dob = input("Date-Of-Birth: ")
    while len(dob) <= 5:
        print(prompt)
        dob = input("Date-Of-Birth: ")
    # to ensure that this field is not empty
    email = input("Email: ")
    while len(email) <= 5:
        print(prompt)
        email = input("Email: ")
    # to ensure that this field is not empty
    city = input("City: ")
    while len(city) <= 1:
        print(prompt)
        city = input("City: ")
    # to ensure that this field is not empty
    state = input("State: ")
    while len(state) < 1:
        print(prompt)
        state = input("State: ")
    # to ensure that this field is not empty
    country = input("Country: ")
    while len(country) <= 2:
        print(prompt)
        country = input("Country: ")
    # to ensure that this field is not empty
    password = input("Create Password at least 12 characters: ")
    while len(password) < 12:
        print("This password is not strong enough")
        password = input("Create Password at least 12 characters: ")
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
    acc_balance = 0
    serial_num = randrange(222222222222222, 999999999999999)
    database [serial_num] = [first_name, lastname, dob, email, city, state, country, password, re_password,
                             account_number, pin, acc_balance]
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
    while loginpassword != (database [serial_num] [8]):
        print("password is incorrect!")
        loginpassword = input("Input your password: ")
    bank_operations(database)


# The main banking startup page
def bank_startup(database):
    print(f"\n\t\t{d} ZIK-BANK {d}")
    acc_option = int(
        input("Welcome to this amazing mobile banking app.\n1.)Create account\n2.)Log in\n\tReply with 1 or 2 > "))
    if acc_option == 1:
        register(database)
    elif acc_option == 2:
        log_in(database)
    else:
        print("Invalid input")
        bank_startup(database)


# The function that holds in all other function
def bank_operations(database):
    print(f"Hello {database [serial_num] [0]} {database [serial_num] [1]} welcome to ZIK-BANK.\n ")
    operation = input(f"what would you like to do today:"
                      f"\n1.)Deposit\n2.)Withdraw\n3.)Check Account balance"
                      f"\n4.)Account Details \n5.)Log-Out\n6.)Exit\n\tReply: ")
    operation = int(operation)
    if operation == 1:
        deposit(database)
    elif operation == 2:
        withdraw(database)
    elif operation == 3:
        balance(database)
    elif operation == 4:
        details(database)
    elif operation == 5:
        bank_startup(database)
    elif operation == 6:
        exit()
    else:
        print("invalid option choosen")
        bank_operations(database)

# The function that accepts user deposit
def deposit(database):
    print(f"{d} Deposit {d}")
    amount = int(input(f"Hello {database [serial_num] [1]} how much would you like to deposit: "))
    pinver = int(input("Input your pin: "))
    if database [serial_num] [-2] == pinver:
        database [serial_num] [-1] += amount
        balance(database)
    else:
        print("Your pin is incorrect")
        deposit(database)
    print()
    opt = input("would you like to check other bank operations 1.) Yes 2.) No : ")
    opt = int(opt)
    if opt == 1:
        bank_operations(database)
    elif opt == 2:
        log_in(database)
    else:
        print("Invalid input")
        log_in(database)

# The withdrawal Function
def withdraw(database):
    print(f"{d} Withdraw {d}")
    database [serial_num] [-1] = int(database [serial_num] [-1])
    print(f"Your balance is {database [serial_num] [-1]}")
    withdrawal_amount = int(input("How much would you like to withdraw: "))
    if withdrawal_amount <= database [serial_num] [-1]:
        withdrawal_pin = int(input("Input your pin: "))
        if withdrawal_pin == database [serial_num] [-2]:
            database [serial_num] [-1] = database [serial_num] [-1] - withdrawal_amount
            print(database [serial_num] [-1])
        else:
            while (withdrawal_pin != database [serial_num] [-2]):
                print("Incorrect Pin")
                print()
                withdraw(database)
    else:
        while (withdrawal_amount > database [serial_num] [-1]):
            print("You do not have up to this amount in your account.")
            withdraw(database)

    print()
    opt = input("would you like to check other bank operations 1.) Yes 2.) No : ")
    opt = int(opt)
    if opt == 1:
        bank_operations(database)
    elif opt == 2:
        log_in(database)
    else:
        print("Invalid input")
        log_in(database)

# The function that holds the user details
def details(database):
    print(f"{d} Your Bank Account Details {d}")
    print(f"Name - {database [serial_num] [0]}-{database [serial_num] [1]}")
    print(f"Date Of Birth - {database [serial_num] [2]}")
    print(f"Email address - {database [serial_num] [3]}")
    print(f"Address - {database [serial_num] [4]},{database [serial_num] [5]},{database [serial_num] [6]}")
    print(f"Password - {database [serial_num] [7]}")
    print(f"Account Number - {database [serial_num] [9]}")
    print(f"Account-balance - {balance(database)}")
    print(f"Pin - *****")
    print()
    opt = input("would you like to check other bank operations 1.) Yes 2.) No : ")
    opt = int(opt)
    if opt == 1:
        bank_operations(database)
    elif opt == 2:
        log_in(database)
    else:
        print("Invalid input")
        bank_startup(database)

# The function that evaluates the user balance
def balance(database):
    print(f"Your balance is ${database [serial_num] [-1]}")
    print()
    opt = input("would you like to check other bank operations 1.) Yes 2.) No : ")
    opt = int(opt)
    if opt == 1:
        bank_operations(database)
    elif opt == 2:
        log_in(database)
    else:
        print("Invalid input")
        log_in(database)


# THE BANK MAIN CALL #
bank_startup(database)