from typing import DefaultDict
import pyperclip
from user import User

def main():
    
    while True:
        print("WELCOME TO PASSWORD LOCKER!!")
        print('\n')
        print("select the following to navigate through: to create new account use 'na': To login your account 'lg' or 'ex' to exit ")
        short_code = input().lower()
        print('\n')

        if short_code == 'na':
            print("create username")
            created_user_name = input()

            print('create password')
            created_user_password = input()

            print('confirm password')
            confirm_password = input()

            while confirm_password != created_user_password:
                print("invalid password did not match")
                print("enter your password")
                created_user_password = input()
                print("confirm your password")
                confirm_password = input()

            else:
                print(f"congratulations {created_user_name}! Account created succesfully")
                print('\n')
                print("proceed to login")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()    

            while entered_username != created_user_name or entered_password != created_user_password:
                print("invalid username or password")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()

            else:
                print(f"Welcome:{entered_username}")
                print('\n')

        elif short_code == 'lg':
            print("welcome")
            print("enter your username")
            default_user_name = input()


            print ("Enter password")
            default_user_password = input()
            print('\n')

            while default_user_name != 'testuser' or default_user_password != '09675':
                print("wrong userName or password. Username 'testuser' and password '09675'")
                print("Enter user name")
                default_user_name = input()

                print("Enter password")
                default_user_password = input()
            

            else: 
                print ("loginsuccess")
                print('\n') 
                print('\n')

        elif short_code == 'ex':
            break
        else:
            print ("enter valid code")  

if __name__ == '__main__':
    
     main()                

