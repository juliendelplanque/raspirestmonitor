#!/bin/python3
""" Little example script of a cmdline interface.

    Author: Julien Delplanque
"""
from raspi_rest_client import *

def main():
    """ Main function of this program.
    """
    up_json = get_pkgs_to_update("192.168.0.10", 5000, "admin", "admin")
    pacman_pkgs_to_update = extract_pacman_pkgs_to_update(up_json)
    print(pacman_pkgs_to_update)
    yaourt_pkgs_to_update = extract_yaourt_pkgs_to_update(up_json)
    print(yaourt_pkgs_to_update)
    s_json = get_sensors_data("192.168.0.10", 5000, "admin", "admin")
    print(s_json)
    system_info = get_system_info("192.168.0.10", 5000, "admin", "admin")
    print(system_info)

if __name__ == '__main__':
    main()
