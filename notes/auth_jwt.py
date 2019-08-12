# pip install Flask-RESTful
# pip install Flask-JWT     (JWT: Json Web Token)

from flask import Flask, request
from flask_restful import Resource, Api      
from flask_jwt import JWT, jwt_required     # jwt_required: decorator

from security import authenticate, identity # these methods are custom made in security.py


app = Flask(__name__)
app.secret_key = 'alsdkfiqowek3948r3qsd9p'  # not sure yet how to handle this 'secret' key
api = Api(app)

jwt = JWT(app, authenticate, identity)      # pass in the security methods

Widgets = []

Class Widget(Resource):     # Inherit Resource
    @jwt_required()     # must authenticate before using this method
    def get(self, ...):
        if widget:
            return widget_info, 200
        else:
            return {'message': "Not found."}, 404

    @jwt_required() 
    def post(self, ...):
        return widget, 201

    @jwt_required() 
    def put(self, ...):
        pass

    @jwt_required() 
    def delete(self, ...):
        pass

api.add_resource(Widget, '/widget/<string:...>')
