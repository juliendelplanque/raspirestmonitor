#!/bin/python3
""" This script contains functions to access to sensors data on a raspberry pi
    running Archlinux. I have no idea if these commands work on other
    distributions.

    Author: Julien Delplanque
"""
import subprocess
def get_temperature():
    """ Return the temperature of the raspberry pi as a float according to its
        temperature sensor.
    """
    proc = subprocess.Popen(["/opt/vc/bin/vcgencmd measure_temp"], stdout=subprocess.PIPE, shell=True)
    (temperature, error) = proc.communicate()
    temperature = temperature.decode("utf-8").split("=")[1]
    return float(temperature[0:len(temperature)-3])

def get_voltage(id: str):
    """ Get the voltage of the component with the id "id" and return it as a
        float.

        Keyword arguments:
        id - the id of the component
    """
    proc = subprocess.Popen(["/opt/vc/bin/vcgencmd measure_volts "+id], stdout=subprocess.PIPE, shell=True)
    (voltage, error) = proc.communicate()
    voltage = voltage.decode("utf-8").split("=")[1]
    return float(voltage[0:len(voltage)-1])

def get_core_voltage():
    """ Return the "core" voltage of the raspberry pi.
    """
    return get_voltage("core")

def get_sdram_core_voltage():
    """ Return the "sdram core" voltage of the raspberry pi.
    """
    return get_voltage("sdram_c")

def get_sdram_io_voltage():
    """ Return the "sdram io" voltage of the raspberry pi.
    """
    return get_voltage("sdram_i")

def get_sdram_physical_voltage():
    """ Return the "sdram physical" voltage of the raspberry pi.
    """
    return get_voltage("sdram_p")