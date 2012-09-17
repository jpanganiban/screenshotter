#!/usr/bin/env python

from flask import Flask, request, jsonify
from screenshooter import config
from pymongo import Connection


app = Flask(__name__)
# Mongodb stuff
conn = Connection()
db = conn[config.MONGO_DB]
db_collection = db[config.MONGO_COLLECTION]
# GEARMAN
client = gearman.GearmanClient(config.GEARMAN_HOSTS)


@app.route('/screenshots', methods=['GET', 'POST'])
def screenshots():
    """Request handler for screenshot requests.

    GET:
    
        Returns all the screenshots:

    {
        result:
        [
            {
                url: <string>
                filename: <file path>
            },
            {
                url: <string>
                filename: <file path>
            }
        ]
    }


    POST:

        Takes in a json object in the form of:

        {
            url: <string>
        }

        Responds with file path of the generated screenshot.

        {
            url: <string>
            filename: <file path>
        }
    """

    if request.method == 'GET':
        screenshots = db_collection.find()
        return jsonify({'result': list(screenshots)})

    if request.method == 'POST':
        data = request.json
        if not data.get('url'):
            return abort(400)
        response = client.submit_job('screenshot', {'url': data.get('url')})
        if response.status == 'FAILED':
            return abort(400)
        # TODO: We need to get the response data.
        return jsonify({'url': '', 'filepath': ''})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
