#!/bin/python3
""" This script contains functions to check wich packages are updatable on the
    system.

    Author: Julien Delplanque
"""
import subprocess
class PackageManagerDoesNotExists(Exception):
    """ Exception launched if the package manager doesn't exists.
    """
    pass

def pacman_packages_to_update():
    """ Return the packages to update from the pacman's database.
    """
    pacman_proc = subprocess.Popen(["/bin/pacman -Qu"], stdout=subprocess.PIPE, shell=True)
    (pacman_out, pacman_err) = pacman_proc.communicate()
    if pacman_proc.returncode == 0:
        pkgs_to_update = pacman_out.decode("utf-8").split("\n")
        pkgs_to_update.pop()
        return pkgs_to_update
    raise PackageManagerDoesNotExists

def yaourt_packages_to_update():
    """ Return the packages to update from the yaourt's database.
    """
    yaourt_proc = subprocess.Popen(["/bin/yaourt -Qu"], stdout=subprocess.PIPE, shell=True)
    (yaourt_out, yaourt_err) = yaourt_proc.communicate()
    if yaourt_proc.returncode == 0:
        pkgs_to_update = yaourt_out.decode("utf-8").split("\n")
        pkgs_to_update.pop()
        return pkgs_to_update
    raise PackageManagerDoesNotExists
