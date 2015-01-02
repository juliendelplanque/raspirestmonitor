# -*- coding: utf-8 -*-

import routes.pkgmanagers.pkgmanagers as pkgmanagers
from flask import jsonify

def create_routes(app, auth):
    @app.route('/pacman', methods = ['GET'])
    @auth.login_required
    def pacman():
        """ Return a json object containing the packages to update.
        """
        try:
            pkgs = pkgmanagers.pacman_packages_to_update()
            return jsonify(pkgs)
        except pkgmanagers.PackageManagerDoesNotExists:
            return jsonify({})

    @app.route('/yaourt', methods = ['GET'])
    @auth.login_required
    def yaourt():
        try:
            pkgs = pkgmanagers.yaourt_packages_to_update()
            return jsonify(pkgs)
        except pkgmanagers.PackageManagerDoesNotExists:
            return jsonify({})
