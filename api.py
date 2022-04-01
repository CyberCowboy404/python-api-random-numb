from flask import Flask, request
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

class RandomNumberApi(Resource):
    def get(self):
        range = request.args.get('range')
        if range and range.isnumeric():
            return random.randint(1, int(range))
        else:
            return random.randint(1, 1000)

api.add_resource(RandomNumberApi, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')