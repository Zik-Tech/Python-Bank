"""
This program is created for banking simulation.
"""
# we import randrange to generate account number
from random import randrange
import data
DESIGN = "~" * 15
database = {}
SERIAL_NUM = 0
ACC_BALANCE = 0
PROMPT = "This field is required"
ERROR = "Invalid input"
OPT_1 = "would you like to check other bank operations 1.) Yes 2.) No : "
ACC_BALANCE = 0
# The function to create an account
def register():
    """
    this function is the one thst handles registration
    and creation of new accounts
    """
    print(f"\n\t\t{DESIGN} CREATE ACCOUNT {DESIGN}")
    first_name = input("First Name: ")
    # to ensure that this field is not empty
    while len(first_name) <= 1:
        print(PROMPT)
        first_name = input("First Name: ")
    # to ensure that this field is not empty
    lastname = input("Last Name: ")
    while len(lastname) <= 1:
        print(PROMPT)
        lastname = input("Last Name: ")
    # to ensure that this field is not empty
    dob = input("Date-Of-Birth: ")
    while len(dob) <= 5:
        print(PROMPT)
        dob = input("Date-Of-Birth: ")
    # to ensure that this field is not empty
    email = input("Email: ")
    while len(email) <= 5:
        print(PROMPT)
        email = input("Email: ")
    # to ensure that this field is not empty
    city = input("City: ")
    while len(city) <= 1:
        print(PROMPT)
        city = input("City: ")
    # to ensure that this field is not empty
    state = input("State: ")
    while len(state) < 1:
        print(PROMPT)
        state = input("State: ")
    # to ensure that this field is not empty
    country = input("Country: ")
    while len(country) <= 2:
        print(PROMPT)
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
        f"Hello {first_name} {lastname} you have successfully created an "
        f"account with us."
        f"\nYour account number is {account_number}"
        f"\nYour account number would be required for all bank operations so "
        f"Keep it safe.\n\n"
    )

    # a serial num for identification in our data-base
    SERIAL_NUM = randrange(222222222222222, 999999999999999)
    database[SERIAL_NUM] = [first_name, lastname, dob, email, city, state, country, password,
    re_password, account_number, ACC_BALANCE,]
    # create a database using the user data
    data.create(SERIAL_NUM, database)

    # redirects to log in function
    log_in()

# The log in function
def log_in():
    """
    this functions handles log-in
    """
    print(database[SERIAL_NUM][3])
    print(f"\n\t\t{DESIGN} LOG-IN {DESIGN}")

    # receive email for log in
    login = input("Input your email: ")
    # check if eail is correct
    while login != (database[SERIAL_NUM][3]):
        print("Incorrect Email.\nTry again")
        login = input("Input Email: ")

    # receive password
    loginpassword = input("Input your password: ")
    # check if password is correct
    while loginpassword != (database[SERIAL_NUM][8]):
        print("password is incorrect!")
        loginpassword = input("Input your password: ")
    bank_operations()


# The main banking startup page
def bank_startup():
    """
    this function runs the register and login function
    it is the function that starts the whole banking program
    """
    print(f"\n\t\t{DESIGN} ZIK-BANK {DESIGN}")
    acc_option = int(
        input(
            "Welcome to this amazing mobile banking app.\n1.)Create "
            "account\n2.)Log in\n\tReply with 1 or 2 > "
        )
    )
    if acc_option == 1:
        register()
    elif acc_option == 2:
        log_in()
    else:
        print(ERROR)
        bank_startup()



def bank_operations():
    """
    this function controls all the banking operations of our program
    """
    print(
        f"Hello {database[SERIAL_NUM][0]} {database[SERIAL_NUM][1]} welcome "
        f"to ZIK-BANK.\n "
    )
    operation = input(
        "what would you like to do today:"
        "\n1.)Deposit\n2.)Withdraw\n3.)Check Account balance"
        "\n4.)Account Details \n5.)Log-Out\n6.)Exit\n\tReply: "
    )
    operation = int(operation)
    if operation == 1:
        deposit()
    elif operation == 2:
        withdraw()
    elif operation == 3:
        balance()
    elif operation == 4:
        details()
    elif operation == 5:
        bank_startup()
    elif operation == 6:
        exit()
    else:
        print("invalid option chosen")
        bank_operations()


# The function that accepts user deposit
def deposit():
    """
    this is the function that control the use's deposit
    """
    print(f"{DESIGN} Deposit {DESIGN}")
    amount = int(
        input(
            f"Hello {database[SERIAL_NUM][1]} how much would you like to " f"deposit: "
        )
    )
    pinver = int(input("Input your pin: "))
    if database[SERIAL_NUM][-2] == pinver:
        database[SERIAL_NUM][-1] += amount
        balance()
    else:
        print("Your pin is incorrect")
        deposit()
    print()
    opt = input(OPT_1)
    opt = int(opt)
    if opt == 1:
        bank_operations()
    elif opt == 2:
        log_in()
    else:
        print(ERROR)
        log_in()


def withdraw():
    """
    this function handles the user withdrawal
    """
    print(f"{DESIGN} Withdraw {DESIGN}")
    database[SERIAL_NUM][-1] = int(database[SERIAL_NUM][-1])
    print(f"Your balance is {database[SERIAL_NUM][-1]}")
    withdrawal_amount = int(input("How much would you like to withdraw: "))
    if withdrawal_amount <= database[SERIAL_NUM][-1]:
        withdrawal_pin = int(input("Input your pin: "))
        if withdrawal_pin == database[SERIAL_NUM][-2]:
            database[SERIAL_NUM][-1] = database[SERIAL_NUM][-1] - withdrawal_amount
            print(database[SERIAL_NUM][-1])
        else:
            while withdrawal_pin != database[SERIAL_NUM][-2]:
                print("Incorrect Pin")
                print()
                withdraw()
    else:
        while withdrawal_amount > database[SERIAL_NUM][-1]:
            print("You do not have up to this amount in your account.")
            withdraw()

    print()
    opt = input(OPT_1)
    opt = int(opt)
    if opt == 1:
        bank_operations()
    elif opt == 2:
        log_in()
    else:
        print("Invalid input")
        log_in()


# The function that holds the user details
def details():
    """
    this function  print the user details
    """
    print(f"{DESIGN} Your Bank Account Details {DESIGN}")
    print(f"Name - {database[SERIAL_NUM][0]}-{database[SERIAL_NUM][1]}")
    print(f"Date Of Birth - {database[SERIAL_NUM][2]}")
    print(f"Email address - {database[SERIAL_NUM][3]}")
    print(
        f"Address - {database[SERIAL_NUM][4]},{database[SERIAL_NUM][5]},"
        f"{database[SERIAL_NUM][6]}"
    )
    print(f"Password - {database[SERIAL_NUM][7]}")
    print(f"Account Number - {database[SERIAL_NUM][9]}")
    print(f"Account-balance - {balance()}")
    print("Pin - *****")
    print()
    opt = input(OPT_1)
    opt = int(opt)
    if opt == 1:
        bank_operations()
    elif opt == 2:
        log_in()
    else:
        print(ERROR)
        bank_startup()


# The function that evaluates the user balance
def balance():
    """
    this function does a simple work of outputing the user balance
    """
    print(f"Your balance is ${database[SERIAL_NUM][-1]}")
    print()
    opt = input(OPT_1)
    opt = int(opt)
    if opt == 1:
        bank_operations()
    elif opt == 2:
        log_in()
    else:
        print(ERROR)
        log_in()


# THE BANK MAIN CALL #
bank_startup()
