#!/bin/python3
""" Little example script of a cmdline interface.

    Author: Julien Delplanque
"""
import argparse
import getpass
import traceback
from raspi_rest_client import *

ERROR_FILE = "error.log"

def main():
    """ Main function of this program.
    """
    # Arguments parsing
    parser = argparse.ArgumentParser(
        description='A simple command line interface for Raspi Rest Monitor.')
    parser.add_argument('-u', '--username', default=None, required=True,
                       help='The username to use for login. Password will be'+
                            ' prompted.')
    parser.add_argument('-a', '--ip-adress', default=None, required=True, dest='ip',
                       help='The ip adress and port of the Raspberry Pi formatted'+
                            ' as ip:port.')
    parser.add_argument('-p', '--pacman', action='store_true',
                       help='Fetch the json containing pacman\'s pkg(s) to'+
                            ' update and print it.')
    parser.add_argument('-y', '--yaourt', action='store_true',
                       help='Fetch the json containing yaourt\'s pkg(s) to'+
                            ' update and print it.')
    parser.add_argument('-s', '--sensors', action='store_true',
                       help='Fetch the json containing sensors data and print'+
                            ' it.')
    parser.add_argument('-i', '--system-info', action='store_true', dest='sysinfo',
                       help='Fetch the json containing system data and print'+
                            ' it.')
    args = parser.parse_args()
    # Work
    ip = args.ip.split(":")[0]
    port = args.ip.split(":")[1]
    password = password = getpass.getpass("Enter the password for "+args.username+": ")
    up_json = get_pkgs_to_update(ip, port, args.username, password)
    if args.pacman:
        pacman_pkgs_to_update = extract_pacman_pkgs_to_update(up_json)
        print(pacman_pkgs_to_update)
    if args.yaourt:
        yaourt_pkgs_to_update = extract_yaourt_pkgs_to_update(up_json)
        print(yaourt_pkgs_to_update)
    if args.sensors:
        s_json = get_sensors_data(ip, port, args.username, password)
        print(s_json)
    if args.sysinfo:
        system_info = get_system_info(ip, port, args.username, password)
        print(system_info)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("The client crashed because of this exception:", type(e).__name__)
        with open(ERROR_FILE, 'w') as error_file:
            error_file.write(traceback.format_exc())
        print("Finished properly, details or error in", ERROR_FILE, ".")
