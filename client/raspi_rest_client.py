#!/bin/python3
""" This script contains functions for the REST client.
    
    Author: Julien Delplanque
"""
import http.client
import json

def get_pacman_pkgs_to_update(ip: str, username: str=None, passwd: str=None):
    """ Get the list of packages from the REST server hosted by
        the raspberry pi.

        TODO implement login.

        Keyword arguments:
        ip       - the ip of the raspberry pi
        username - your username
        passwd   - your password
    """
    conn = http.client.HTTPConnection(ip+":5000")
    conn.request("GET", "/pkgtoupdate")
    response = conn.getresponse()
    j = json.loads(response.read().decode("utf-8"))
    return j.get("pacman")

def get_sensors_data(ip: str, username: str=None, passwd: str=None):
    """ Get the list of sensors data from the REST server hosted by
        the raspberry pi.

        TODO implement login.
        
        Keyword arguments:
        ip       - the ip of the raspberry pi
        username - your username
        passwd   - your password
    """
    conn = http.client.HTTPConnection(ip+":5000")
    conn.request("GET", "/sensors")
    response = conn.getresponse()
    return json.loads(response.read().decode("utf-8"))
