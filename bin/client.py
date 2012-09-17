#!/usr/bin/env python

from sys import argv
from screenshooter import config
from screenshooter import custom_gearman as gearman


client = gearman.GearmanClient(config.GEARMAN_HOSTS)


def show_help():
    print """Screenshotter:
You enter multiple urls separated by spaces.

eg.
client http://www.jpanganiban.com/ http://www.plurk.com/ http://www.google.com/
    """


def main():
    # Take arguments
    if len(argv) < 2:
        show_help()
    urls = argv[1:]
    if 'help' in urls:
        show_help()
        return 0
    # TODO: Validate url
    responses = []
    for url in urls:
        response = client.submit_job('screenshot', {'url': url})
        print response
        responses.append(response)
    return 0


if __name__ == '__main__':
    main()
