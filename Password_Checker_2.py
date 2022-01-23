"""
PSEUDOCODE
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10
INPUT Password
WHILE len(PASSWORD) < MIN_PASSWORD_LENGTH or > MAX_PASSWORD_LENGTH
IF Password.isalpha() or Password.isnumeric() or Password.isalnum()
OUTPUT message
ELSE
OUTPUT message
"""
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10

Password = input("Please input your password: ")
while len(Password) < MIN_PASSWORD_LENGTH or len(Password) > MAX_PASSWORD_LENGTH:
    print("The password you've entered is incorrect, your password should between 6 and 10 characters.")
    Password = input("Please input your password: ")
if Password.isalpha():
    print("Invalid password. Your password only contains letters")
elif Password.isnumeric():
    print("Invalid password. Your password only contains numbers")
else:
    print("Your password is strong")

"""
The coding structure I have used here is checking for multiple things.
The first part of the code is a while loop. So the code is saying that while the length of the password is less than
the MIN_PASSWORD_LENGTH of 6 or greater than the MAX_PASSWORD_LENGTH of 10, it will print out a message saying that the
the password should be between 6 and 10 characters. The last 3 parts of the code is checking to see if the password is
either completely made up of letters or numbers. The last line of the code is simply saying that if the conditions of
an alphanumeric password between 6 and 10 characters, the code will print out a message saying that the password is
strong.
"""