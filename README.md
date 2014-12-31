Raspi REST monitor
================

Simply a REST server and a REST client to fetch data from your raspberry pi.

Data that the REST API provide now:
- packages updates needed (only for pacman and yaourt currently)
- sensors data
- system info (may not work on other distributions than Archlinux)

If you try this on another distribution, it may or may not work, I didn't
test it already.

This program is really young, it will be improved by the time ;)

TODO:
- ~~Implement login on both server and client side~~
- Fully manage requests errors
- Support other distribs
- Add more interfaces
- Create a setup script that configure the server
- ~~Find a way to manage and save securely passwords on the server~~

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
- Install bcrypt
~~~
pip install bcrypt
~~~
- Clone the repository
- Launch an interface with python3.

For example, this will output pacman's packages to update and sensors data:
~~~
/bin/python3 raspirestmonitor/client/cmd_interface.py --username 'user' --ip-adress '192.168.X.Y:5000' --pacman --sensors

~~~

Create your own interface!
==========================

You have all the stuff you need to create you own interface to the rest client
in the /client directory :)
