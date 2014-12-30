#!/bin/python3
"""
"""
from passwordmanagement import PasswordManager
import getpass

def main():
    password_manager = PasswordManager(".raspirestpass")
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")
    password_manager.add_user(username, password.encode("utf-8"))
    password_manager.write()

if __name__ == '__main__':
    main()
