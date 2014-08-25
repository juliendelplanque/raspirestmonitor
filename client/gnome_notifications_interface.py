#!/bin/python3
""" This script is an exemple of interface for the REST client.
    It inform the user of changes using gnome's notifications.

    Author: Julien Delplanque
"""
from gi.repository import Notify
import time
from raspi_rest_client import *

GREETING="Dear sir,"
SAY_GOODBYE="Sincerly, your raspberry pi."

def format_message(pkgs: list):
    """ Format a message to display to the user using the list of the packages
        to update.

        Keyword arguments:
        pkgs - the list of package to update
    """
    message = GREETING + "\n"
    message += "You have to know that these packages request an update:\n"
    for pkg in pkgs:
        message += "\t"+pkg + "\n "
    message += "\n"+SAY_GOODBYE
    return message

def main():
    """ Main function of this program.
    """
    up_json = get_pkgs_to_update("192.168.0.10", 5000, "admin", "admin")
    pacman_pkgs_to_update = extract_pacman_pkgs_to_update(up_json)
    yaourt_pkgs_to_update = extract_yaourt_pkgs_to_update(up_json)
    s_json = get_sensors_data("192.168.0.10", 5000, "admin", "admin")
    print(s_json)
    if len(pacman_pkgs_to_update) > 0:
        message = format_message(pacman_pkgs_to_update)
        Notify.init("Raspi updates")
        notification = Notify.Notification.new("Raspi updates", message)
        notification.show()
        time.sleep(30) # The notification will stay 30 seconds
        notification.close()

if __name__ == '__main__':
    main()
