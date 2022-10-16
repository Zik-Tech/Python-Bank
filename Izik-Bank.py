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
    print(len(pin))
    # to check if the pin created is 5 digit
    while len(pin) < 5 or len(pin) > 5:
        print("Your pin is not of required standard")
        pin = input("Create a 'Five' digit pin for transaction: ")
    pin = int(pin)

    print(
        f"Hello {first_name} {lastname} you have successfully created an account with us.\nYour account number is {account_number}\nYour account number would be required for all bank operations so Keep it safe.\n\n")
    # a serial num for identification in our data-base
    global serial_num
    serial_num = randrange(222222222222222, 999999999999999)
    database [serial_num] = [first_name, lastname, dob, email, city, state, country, password, re_password,
                             account_number, pin]
    print(database[serial_num][3])
    log_in(database)


# The log in function
def log_in(database):
    print(f"\n\t\t{d} LOG-IN {d}")
    #print(database.items([serial_num][3]))
    # login = input("Input account number or email: ")
    # while login != database[serial_num][3] or database.values([serrial])


# The main banking function
def bank_operation():
    print(f"\n\t\t{d} ZIK-BANK {d}")
    acc_option = int(
        input("Welcome to this amazing mobile banking app.\n1.)Create account\n2.)Log in\n\tReply with 1 or 2 > "))
    if acc_option == 1:
        register()
    elif acc_option == 2:
        log_in(database)
    else:
        print("Invalid input")
        bank_operation()


# THE BANK MAIN CALL #
bank_operation()
