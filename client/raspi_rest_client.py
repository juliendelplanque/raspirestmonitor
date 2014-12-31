#!/bin/python3
""" This script contains functions for the REST client.

    Author: Julien Delplanque
"""
import requests
import json

class UnknownUserException(Exception):
    pass

class ServerErrorException(Exception):
    pass

def make_request(ip: str, port: int, username: str, passwd: str, service: str):
    """ Make a request to the specified service of the server.

        Keyword arguments:
        ip       - the ip of the raspberry pi
        username - your username
        passwd   - your password
        service  - the service you want to contact
    """
    url = "http://"+ip+":"+str(port)+"/"+service
    response = requests.get(url, auth=(username, passwd))
    if response.status_code == 401:
        raise UnknownUserException(response.text)
    elif response.status_code == 500:
        raise ServerErrorException(response.text)
    return json.loads(response.text)

def get_pkgs_to_update(ip: str, port: int, username: str, password: str):
    """ Get the list of packages from the REST server hosted by
        the raspberry pi.

        Keyword arguments:
        ip       - the ip of the raspberry pi
        port     - the port the server is listening to
        username - your username
        password - your password
    """
    return make_request(ip, port, username, password, "pkgtoupdate")

def extract_pacman_pkgs_to_update(json: dict):
    """ Extract the list of pacman's packages from the json passed in parameters.

        Keyword arguments:
        json - a dict that represent the json
    """
    return json.get('pacman')

def extract_yaourt_pkgs_to_update(json: dict):
    """ Extract the list of yaourt's packages from the json passed in parameters.

        Keyword arguments:
        json - a dict that represent the json
    """
    return json.get('yaourt')

def get_sensors_data(ip: str, port: int, username: str, password: str):
    """ Get the list of sensors data from the REST server hosted by
        the raspberry pi.

        Keyword arguments:
        ip       - the ip of the raspberry pi
        port     - the port the server is listening to
        username - your username
        password - your password
    """
    return make_request(ip, port, username, password, "sensors")

def get_system_info(ip: str, port: int, username: str, password: str):
    """ Get system information from the REST server hosted by the raspberry pi.

        Keyword arguments:
        ip       - the ip of the raspberry pi
        port     - the port the server is listening to
        username - your username
        password - your password
    """
    return make_request(ip, port, username, password, "systeminfo")
