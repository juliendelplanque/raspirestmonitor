#!/bin/python3
""" This script create a file containing a json with usernames as keys
    and hashed passwords as values.

    Author: Julien Delplanque
"""
from passwordmanagement import PasswordManager
import getpass

def main():
    password_manager = PasswordManager(".raspirestpass")
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")
    # The password encoding is raspberry-pi specific
    password_manager.add_user(username, password.encode("utf-8"))
    password_manager.write()

if __name__ == '__main__':
    main()
