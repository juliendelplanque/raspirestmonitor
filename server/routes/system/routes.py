# -*- coding: utf-8 -*-

import routes.system.systeminfo as systeminfo
from flask import jsonify

def create_routes(app, auth):
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
