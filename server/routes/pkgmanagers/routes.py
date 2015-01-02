# -*- coding: utf-8 -*-

import routes.pkgmanagers.pkgmanagers as pkgmanagers
from flask import jsonify

def create_routes(app, auth):
    @app.route('/pkgtoupdate', methods = ['GET'])
    @auth.login_required
    def pkg_to_update():
        """ Return a json object containing the packages to update.
        """
        dic = {}
        try:
            pkgs = pkgmanagers.pacman_packages_to_update()
            dic['pacman'] = pkgs
        except pkgmanagers.PackageManagerDoesNotExists as e:
            print(e)
        try:
            pkgs = pkgmanagers.yaourt_packages_to_update()
            dic['yaourt'] = pkgs
        except pkgmanagers.PackageManagerDoesNotExists as e:
            print(e)
        return jsonify(dic)
