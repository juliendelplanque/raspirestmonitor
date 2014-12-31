#!/bin/python3
""" This script contains the implementation of the REST api on the
    raspberry-pi.

    Author: Julien Delplanque
"""
import subprocess
from flask import Flask, jsonify, Response
from flask.ext.httpauth import HTTPBasicAuth
import sensors
import pkgmanagers
import systeminfo
from passwordmanagement import PasswordManager

app = Flask(__name__)
auth = HTTPBasicAuth()
password_manager = PasswordManager(".raspirestpass")

@auth.verify_password
def verify_password(username, password):
    return password_manager.is_correct(username, password)

@auth.error_handler
def unauthorized():
    return Response("You are not authorized to access this resource.", 401)

@app.route('/pkgtoupdate', methods = ['GET'])
@auth.login_required
def pkg_to_update():
    """ Return a json object containing the packages to update.
    """
    dic = {}
    try:
        pkgs = pkgmanagers.pacman_packages_to_update()
        dic['pacman'] = pkgs
    except PackageManagerDoesNotExists as e:
        print(e)
    try:
        pkgs = pkgmanagers.yaourt_packages_to_update()
        dic['yaourt'] = pkgs
    except PackageManagerDoesNotExists as e:
        print(e)
    return jsonify(dic)

@app.route('/sensors', methods = ['GET'])
@auth.login_required
def sensors_data():
    """ Return a json object containing the sensors and their data.
    """
    return jsonify({'temperature': sensors.get_temperature(),
                    'core_voltage': sensors.get_core_voltage(),
                    'sdram_core_voltage': sensors.get_sdram_core_voltage(),
                    'sdram_io_voltage': sensors.get_sdram_io_voltage(),
                    'sdram_physical_voltage': sensors.get_sdram_physical_voltage()})

@app.route('/systeminfo', methods = ['GET'])
@auth.login_required
def system_info():
    """ Return a json object containing various informations about the system.
    """
    return jsonify({'uptime': str(systeminfo.get_uptime()),
                    'idletime': str(systeminfo.get_idletime()),
                    'total_ram': systeminfo.get_total_ram(),
                    'free_ram': systeminfo.get_free_ram(),
                    'used_ram': systeminfo.get_used_ram(),
                    'kernel_version': systeminfo.get_kernel_version(),
                    'kernel_build_date': systeminfo.get_kernel_build_date()})

if __name__ == '__main__':
    password_manager.load()
    app.run(host="0.0.0.0")
