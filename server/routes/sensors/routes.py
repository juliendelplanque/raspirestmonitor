# -*- coding: utf-8 -*-

import routes.sensors.sensors as sensors
from flask import jsonify

def create_routes(app, auth):
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
