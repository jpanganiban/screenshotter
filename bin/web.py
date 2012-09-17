#!/usr/bin/env python

from flask import Flask, request, jsonify
from screenshooter import config
from pymongo import Connection


app = Flask(__name__)
# Mongodb stuff
conn = Connection()
db = conn[config.MONGO_DB]
db_collection = db[config.MONGO_COLLECTION]


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
        # TODO: Should return screenshots
        return jsonify({'result': []})

    if request.method == 'POST':
        data = request.json
        # TODO: Send data to worker


if __name__ == '__main__':
    app.run()
