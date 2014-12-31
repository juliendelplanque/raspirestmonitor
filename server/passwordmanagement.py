#!/bin/python3
# -*- coding: utf-8 -*-
""" This script contains the class PasswordManager that is usefull for password
    secure storage.
    This article has been usefull to write this script:
        http://throwingfire.com/storing-passwords-securely/

    Author: Julien Delplanque
"""
import bcrypt
import json

class PasswordManager(object):
    """ This object allow you to easily manipulate a password database stored
        in a file as a json.
        This json contain username: digest couples.
    """
    def __init__(self, file_path: str):
        """ Initialize the PasswordManager.
            This method does not load the file where the password are stored,
            you have to explicitely call the load method on this object.

            Keyword arguments:
            file_path - the path of the password file
        """
        self.password_file_path = file_path
        self.password_dic = {}

    def add_user(self, username: str, password: str):
        """ Add a couple of username, password to the database.
            This method does not modify the file, you have to explicitly call
            the write method on this object to modify the file.

            Keyword arguments:
            username - the username as a string
            password - the password as a string
        """
        self.password_dic[username] = str(bcrypt.hashpw(password, bcrypt.gensalt()))

    def is_correct(self, username: str, password: str):
        """ Determinate if a couple of username, password is correct according
            to the password database.

            Keyword arguments:
            username - the username as a string
            password - the password as a string
        """
        if username in list(self.password_dic.keys()):
            expected_digest = self.password_dic[username]
            password_bytes = password.encode("utf-8")
            salt_bytes = self.password_dic[username].encode("utf-8")
            digest = bcrypt.hashpw(password_bytes, salt_bytes)
            # Here the decode is raspberry-pi specific
            if digest.decode("utf-8") == expected_digest:
                return True
        return False

    def write(self):
        """ Write the json in the password file.
        """
        with open(self.password_file_path, "w+") as password_file:
            password_file.write(json.dumps(self.password_dic))

    def load(self):
        """ Read the json from the password file and set the password_dic
            variable according to the json.
        """
        with open(self.password_file_path, "r") as password_file:
            self.password_dic = json.loads(password_file.read())
        # These next lines are raspberry-pi specific
        for key in self.password_dic.keys():
           self.password_dic[key] = self.password_dic[key][2:len(self.password_dic[key])-1]
