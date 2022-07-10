from flask import Flask, redirect, request
from flask_restful import Resource, Api, reqparse
from dbManager import SQDBManager
from hashlib import sha256
# Simport pandas as pd
# import ast


app = Flask(__name__)
api = Api(app)
db = SQDBManager()

class Create(Resource):
    def post(self):
        # get arguments from the header of the request
        if 'url' not in request.headers:
            return {'message': 'No url provided'}, 400
        url = reqparse.request.headers['url']

        alias = ""
        ttl = 0

        # alias provided by user
        if 'alias' in request.headers:
            # Check if the alias already exists
            if db.get(request.headers['alias']) is not None:
                return {"error": "Alias already exists"}, 400
            alias = request.headers['alias']
        # alias must be created by Pyly
        else:
            alias = db.get_alias(url)
            if alias is not None:
                return {"error": "Alias already exists",
                        "alias": alias}, 400
            else:
                # hash the url and use the first 6 chars as alias
                alias = sha256(request.headers['url'].encode('utf-8')).hexdigest()[:6]

        if 'ttl' in request.headers:
            ttl = request.headers['ttl']

        # add the url to the database
        db.add(url, alias, ttl)
        return {"alias": alias}, 201

class Redirect(Resource):
    def get(self, alias):
        # get the url from the database
        url = db.get(alias)
        if url is None:
            return {"error": "Alias does not exist"}, 404
        url = "http://" + url[1]

        # redirect to the url
        return redirect(url, code=302)

api.add_resource(Create, '/create')  # '/create' is our entry point
api.add_resource(Redirect, '/r/<alias>')  # '/create' is our entry point


if __name__ == '__main__':
    app.run()  # run our Flask app