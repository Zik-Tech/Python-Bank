"""
this is the file that processes all user data CRUD
"""


def create(serial_num, database):
    """
    this function  stores the user input after accont creation
    """
    try:
        f = open("Database/" + str(serial_num) + ".txt", "x")
        f.write(str(database))
        f.close()
    except FileExistsError:
        print("This user already exist")


def read(serial_num):
    """
    this function read the file to get stored input
    """
    try:
        fr = open("Database/" + str(serial_num) + ".txt", "r")
        f_r = fr.read()
        fr.close()
        return f_r
    except FileNotFoundError:
        print("User does not exist")
