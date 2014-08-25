#!/bin/python3
""" This script contains functions to access various system's info.

    Author: Julien Delplanque
"""
import subprocess
from datetime import timedelta

def get_uptime():
    """ Return the uptime of the system as a timedelta object.
    """
    proc = subprocess.Popen(["cat /proc/uptime"],
                            stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    uptime = int(output.decode("utf-8").split()[0].split(".")[0])
    s = uptime % 60
    m = int((uptime/60) % 60)
    h = int((uptime/(60*60) % 24))
    return timedelta(hours=h, minutes=m, seconds=s)

def get_idletime():
    """ Return the idle time of the system as a timedelta object.
    """
    proc = subprocess.Popen(["cat /proc/uptime"],
                            stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    idletime = int(output.decode("utf-8").split()[1].split(".")[0])
    s = idletime % 60
    m = int((idletime/60) % 60)
    h = int((idletime/(60*60) % 24))
    return timedelta(hours=h, minutes=m, seconds=s)
