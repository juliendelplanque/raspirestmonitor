#!/bin/python3
""" This script contains the implementation of the REST api on the
    raspberry-pi.

    Author: Julien Delplanque
"""
import subprocess
from flask import Flask, jsonify
import sensors
import pkgmanagers

app = Flask(__name__)

@app.route('/pkgtoupdate', methods = ['GET'])
def pkg_to_update():
    """ Return a json object containing the packages to update.
    """
    dic = {}
    try:
        pkgs = pkgmanagers.pacman_packages_to_update()
        dic['pacman'] = pkgs
    except:
        pass
    try:
        pkgs = pkgmanagers.yaourt_packages_to_update()
        dic['yaourt'] = pkgs
    except:
        pass
    return jsonify(dic)

@app.route('/sensors', methods = ['GET'])
def sensors_data():
    """ Return a json object containing the sensors and their data.
    """
    return jsonify({'temperature': sensors.get_temperature(),
                    'core_voltage': sensors.get_core_voltage(),
                    'sdram_core_voltage': sensors.get_sdram_core_voltage(),
                    'sdram_io_voltage': sensors.get_sdram_io_voltage(),
                    'sdram_physical_voltage': sensors.get_sdram_physical_voltage()})

if __name__ == '__main__':
    app.run(host="0.0.0.0")