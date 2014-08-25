#!/bin/python3
""" This script contains functions to access various system's info.

    Author: Julien Delplanque
"""
import subprocess

def get_uptime():
    """ Return the uptime of the system as a str using the command: $ uptime
    """
    proc = subprocess.Popen(["uptime"], stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    uptime = output.decode("utf-8").split(",")[0]
    uptime = uptime[uptime.find("up")+3:len(uptime)] # extract uptime
    return uptime
