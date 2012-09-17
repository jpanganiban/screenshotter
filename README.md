Screenshooter
=============

##Requirements

Gearman
Python
PhantomJS
MongoDB

##Installation

    cd screenshooter

    python setup.py develop

Optional

    ln -s /path/to/screenshooter/bin/worker.py /usr/local/bin/worker.py
    ln -s /path/to/screenshooter/bin/client.py /usr/local/bin/client.py
    ln -s /path/to/screenshooter/bin/web.py /usr/local/bin/web.py

##Usage

First, you need to run the worker.

    cd /path/to/screenshooter/bin
    ./worker.py

Next, you can use the shell client:

    cd /path/to/screenshooter/bin
    ./client.py [urls]

You can also run the web interface:

    cd /path/to/screenshooter/bin
    ./web.py
    > * Running on http://0.0.0.0:8080/

##Configuration

You can edit the config.py to set you variables.

    cd /path/to/screenshooter/src/
    vim config.py
