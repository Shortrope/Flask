from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required     # jwt_required: decorator

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'josie'
api = Api(app)

jwt = JWT(app, authenticate, identity)      # creates /auth end point

items = []

class Item(Resource):
    @jwt_required()     # nust authenticate before using 'get' method
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item w name '{}' exists.".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass


class ItemList(Resource):
    def get(self):
        if items:
            return {'items': items}
        return {'items': None}, 404

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(host='192.168.1.10', port=5000, debug=True)

