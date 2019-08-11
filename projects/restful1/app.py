import random
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


suggestions = []


class Suggestion(Resource):
    def get(self):
        if suggestions:
            return {'suggestion': random.choice(suggestions)}
        return {'suggestion': None}, 404

    def post(self):
        data = request.get_json()
        if data['suggestion'] in suggestions:
            return {'suggestion': "Already exists"}, 400
        suggestions.append(data['suggestion'])
        return data

    def delete(self):
        data = request.get_json()
        if data['suggestion'] in suggestions:
            suggestions.remove(data['suggestion'])
            return {'suggestion': "Removed"}
        return {'suggestion': "'{}' is not in the list.".format(data['suggestion'])}, 400


class Suggestions(Resource):
    def get(self):
        if suggestions:
            return {'suggestions': suggestions}
        return {'suggestions': None}, 404

api.add_resource(Suggestion, '/suggestion')
api.add_resource(Suggestions, '/suggestions')

app.run(host='192.168.1.10', port=5000)
