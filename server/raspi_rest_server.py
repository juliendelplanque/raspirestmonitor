#!/bin/python3
""" This script contains the implementation of the REST api on the
    raspberry-pi.

    Author: Julien Delplanque
"""
import imp
import os
import subprocess
from flask import Flask, jsonify, Response
from flask.ext.httpauth import HTTPBasicAuth

from passwordmanagement import PasswordManager

app = Flask(__name__)
auth = HTTPBasicAuth()
password_manager = PasswordManager(".raspirestpass")

@auth.verify_password
def verify_password(username, password):
    return password_manager.is_correct(username, password)

@auth.error_handler
def unauthorized():
    return Response("You are not authorized to access this resource.", 401)

def load_routes(app, auth):
    """ Load dynamically routes in ./routes directory.
    """
    routes_directories = [d for d in os.listdir("routes") if os.path.isdir(os.path.join("routes", d))]
    for route_directory in routes_directories:
        module_path = os.path.join("routes", route_directory, "routes.py")
        if(os.path.exists(module_path)):
            print("Loading", route_directory) # TODO use logging
            module = imp.load_source("./routes", module_path)
            module.create_routes(app, auth)

if __name__ == '__main__':
    password_manager.load()
    load_routes(app, auth)
    app.run(host="0.0.0.0")
