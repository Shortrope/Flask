from flask import Flask, request
from flask_restful import Resource, Api, reqparser
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

    #@jwt_required()
    def delete(self, name):
        #for item in items:
            #if name == item['name']:
                #items.remove(item)
                #return {"name": "Removed"}
        #return {"name": "Not found"}, 400

        # items.remove(item: item in items if item['name'] == name)

        global items
        items = list(filter(lambda item: item['name'] != name, items))
        return {"name": "Removed"}

    def put(self, name):
        #data = request.get_json()
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank!"
        )
        data = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            #item['price'] = data['price']
            item.update(data)
            return item
        else:
            item = {'name': name, 'price': data['price']}
            items.append(item)
            return item, 201


class ItemList(Resource):
    def get(self):
        if items:
            return {'items': items}
        return {'items': None}, 404

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(host='192.168.1.10', port=5000, debug=True)

