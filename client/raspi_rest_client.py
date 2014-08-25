#!/bin/python3
""" This script contains functions for the REST client.

    Author: Julien Delplanque
"""
import requests
import json

class UnknownUserException(Exception):
    pass

def get_pkgs_to_update(ip: str, port: int, username: str, passwd: str):
    """ Get the list of packages from the REST server hosted by
        the raspberry pi.

        Keyword arguments:
        ip       - the ip of the raspberry pi
        username - your username
        passwd   - your password
    """
    url = "http://"+ip+":"+str(port)+"/pkgtoupdate"
    response = requests.get(url, auth=(username, passwd))
    if response.status_code == 401:
        raise UnknownUserException()
    return json.loads(response.text)

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

def get_sensors_data(ip: str, port: int, username: str=None, passwd: str=None):
    """ Get the list of sensors data from the REST server hosted by
        the raspberry pi.

        TODO implement login.

        Keyword arguments:
        ip       - the ip of the raspberry pi
        username - your username
        passwd   - your password
    """
    url = "http://"+ip+":"+str(port)+"/sensors"
    response = requests.get(url, auth=(username, passwd))
    # TODO check if everything went ok
    return json.loads(response.text)
