#!/bin/python3
""" This script contains functions to access various system's info.

    Author: Julien Delplanque
"""
import subprocess
from datetime import timedelta
from datetime import datetime

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

def get_total_ram():
    """ Return the total amount of ram of the system in kB as an integer.
    """
    proc = subprocess.Popen(["cat /proc/meminfo"],
                            stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    ram_info = output.decode("utf-8").split("\n")
    return int(ram_info[0].split()[1])

def get_free_ram():
    """ Return the amount of free ram of the system in kB as an integer.
    """
    proc = subprocess.Popen(["cat /proc/meminfo"],
                            stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    ram_info = output.decode("utf-8").split("\n")
    return int(ram_info[1].split()[1])

def get_used_ram():
    """ Return the amount of used ram on the system in kB as an integer.
    """
    return get_total_ram() - get_free_ram()

def get_kernel_version():
    """ Return a str containing the kernel version.
    """
    proc = subprocess.Popen(["cat /proc/version"],
                            stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    version = output.decode("utf-8").split()[2]
    return version

def get_kernel_build_date():
    """ Return a str containing the kernel's build date.
    """
    proc = subprocess.Popen(["cat /proc/version"],
                            stdout=subprocess.PIPE, shell=True)
    (output, error) = proc.communicate()
    raw_list = output.decode("utf-8").split()
    (year, month, day) = (raw_list[-1], raw_list[-5], raw_list[-4])
    time = raw_list[-3]
    str_date = day+" "+month+" "+year+" - "+time
    # convert to a datetime object?
    return str_date
