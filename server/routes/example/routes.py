# -*- coding: utf-8 -*-

import routes.example.requested

def create_routes(app, auth):
    @app.route('/example', methods = ['GET'])
    def example():
        return routes.example.requested.get_example()
