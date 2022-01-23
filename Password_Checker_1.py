"""
PSEUDOCODE
INPUT Password
IF Password == isnumeric()
PASSWORD = WEAK
ELIF password == isalpha()
PASSWORD = WEAK
ELIF Password isalpha() & isnumeric()
PASSWORD = STRONG
OUTPUT message
"""
Password = input("Please input your password: ")
if Password.isnumeric():
    print("Your password is weak - it contains only numbers")
elif Password.isalpha():
    print("Your password is weak - it contains only letters")
elif Password.isalnum():
    print("Your password is strong")

"""
The coding structure I have used here is checking for three different things.
The first line of code is asking the user to input their password from their keyboard.
The second line of code checks the input to see if the password contains only numeric characters, if so,
the code prints out that the password is weak and that it only contains numbers. 
The third line of code checks the input to see if the password contains only alphabetic characters, if so,
the code prints out that the password is weak and that it only contains letters.
The last line of code checks the input to see if the passwords contains both alphabetic and numeric characters, if so
the code prints out that the password is strong.
"""