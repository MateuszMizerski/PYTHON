import os
import re
import selenium
#class web_page:


def get_login_and_password(option = "load_cfg"):
    password = 'None'
    login = 'None'
    if (option == "default"):
        print("Enter your login:")
        login = input()
        print("Enter your password:")
        password = input()
    else:
        try:
            file = open("F:\\PYTHON\\cfg.txt")
        except IOError:
            print("File is not readable")
        finally:
            for line in file:
                args = line.split()
                if (re.search("password",line)):
                    password = args[1]
                if (re.search("login",line)):
                    login = args[1]
    print(login,password)
    return login,password

class web_page:
    def __init__(self,login,password,page):
        self.login = login
        self.password = password
        self.page = page
    def log_in(self):
        print("Here will be done login into the page")

    def __del__(self):
        print("Destructor called")

if __name__ == "__main__":
    print("XD")
    login,password = get_login_and_password()