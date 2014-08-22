Raspi REST monitor
================

Simply a REST server and a REST client to monitor package updates needed, temperature and voltage of your raspberry-pi.

Currently only work on for raspberry-pi running Archlinux.

TODO:
- Implement login on both server and client side.
- Support other distribs
- Add more interfaces

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
- Install flask using pip
~~~
pip install Flask
~~~
- Clone the repository
- Launch an interface with python3:
~~~
/bin/python3 raspirestmonitor/client/gnome_notifications_interface.py
~~~
