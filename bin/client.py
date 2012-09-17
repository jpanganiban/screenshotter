#!/usr/bin/env python

from sys import argv
from screenshooter import config, utils
from screenshooter import custom_gearman as gearman
from pymongo import Connection


client = gearman.GearmanClient(config.GEARMAN_HOSTS)
# Mongodb stuff
conn = Connection()
db = conn[config.MONGO_DB]
db_collection = db[config.MONGO_COLLECTION]


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
        if response.state == 'COMPLETE':
            data = {'url': url, 'filename': utils.save_path(response.job.unique)}
            responses.append(response)
    # TODO: Store in database.
    if config.USE_MONGO:
        db_collection.insert(responses)
    return {'result': responses}


if __name__ == '__main__':
    main()
