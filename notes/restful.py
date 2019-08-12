# pip install Flask-RESTful

# http responses:
# 200 Ok
# 201 Created
# 400 Bad Request
# 401 UnAuthorized
# 404 Not Found

from flask import Flask, request
from flask_restful import Resource, Api      

app = Flask(__name__)
api = Api(app)

Class Widget(Resource):     # Inherit Resource
    def get(self, ...):
        if widget:
            return widget_info, 200
        else:
            return {'message': "Not found."}, 404

    def post(self, ...):
        return widget, 201

    def put(self, ...):
        pass

    def delete(self, ...):
        pass

api.add_resource(Widget, '/widget/<string:...>')
