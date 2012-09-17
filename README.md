Screenshooter
=============

##Requirements

Gearman
Python
PhantomJS
MongoDB
libevent

##Installation

    cd screenshooter

    python setup.py develop/install

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

You can also run the web interface [unfinished]:

    cd /path/to/screenshooter/bin
    ./web.py
    > * Running on http://0.0.0.0:8080/

Web also acts as a RESTful interface for the screenshooter.

##Configuration

You can edit the config.py to set you variables.

    cd /path/to/screenshooter/src/
    vim config.py

##Unfinished Features

- Run on multiple threads/greenlets
    Was not sure if gearman is gevent safe (monkey_patchable)

- Test scripts
    Failed to write tests. :(

- Screenshot_done queue was not completed.
    Instead, used Mongodb for persistent storage.

- Web interface
    Already have the RESTful API.
