def main():
    MIN_PASSWORD_LENGTH = 6
    MAX_PASSWORD_LENGTH = 10
    PASSWORD_LOG_FILE = "password_log.txt"
    import datetime
    DATETIME = str(datetime.datetime.today())
    Password_Log_File_Opening = open(PASSWORD_LOG_FILE,"a")

    Password = input("Please input your password: ")
    while len(Password) < MIN_PASSWORD_LENGTH or len(Password) > MAX_PASSWORD_LENGTH:
        print("The password you've entered is incorrect, your password should between 6 and 10 characters.")
        if len(Password) < MIN_PASSWORD_LENGTH:
            reason_password_invalid = "Password < 6"
        elif len(Password) > MAX_PASSWORD_LENGTH:
            reason_password_invalid = "Password > 10"
        else:
            print("Your password is strong")
        Password = input("Please input your password: ")
    Password_Log_File_Opening.write(DATETIME)
    Password_Log_File_Opening.write(", ")
    Password_Log_File_Opening.write(reason_password_invalid)
    Password_Log_File_Opening.write("\n")
    Password_Log_File_Opening.close()

    Password_Log_File_Opening = open(PASSWORD_LOG_FILE,"r")
    for line in Password_Log_File_Opening:
        print(line)


main()