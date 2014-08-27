Raspi REST monitor
================

Simply a REST server and a REST client to monitor package updates needed, temperature and voltage of your raspberry-pi.

Currently only work on for raspberry-pi running Archlinux.

This program is really young, it will be improved by the time ;)

TODO:
- ~~Implement login on both server and client side~~
- Manage requests errors
- Support other distribs
- Add more interfaces
- Create a setup script that configure the server
- Find a way to manage and save securely passwords on the server

Installation:
============

*Server:*

I suppose you already have a cron task that update the pacman's package cache (pacman -Sy) running on your system :)

- Install pip
~~~
pacman -S python-pip
~~~
- Install flask using pip
~~~
pip install Flask
~~~
- Clone the repository
- Launch the server with python3:
~~~
/bin/python3 raspirestmonitor/server/raspi_rest_server.py
~~~

*Client:*

- Install pip
~~~
pacman -S python-pip
~~~
- Install requests using pip
~~~
pip install requests
~~~
- Clone the repository
- Launch an interface with python3:
~~~
/bin/python3 raspirestmonitor/client/gnome_notifications_interface.py
~~~

Create your own interface!
==========================

You have all the stuff you need to create you own interface to the rest client
in the /client directory :)
