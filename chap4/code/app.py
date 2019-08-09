from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        if items:
            for item in items:
                if name == item['name']:
                    return item
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.99}
        items.append(item)
        return item, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass

api.add_resource(Item, '/item/<string:name>')

app.run(host='192.168.1.10', port=5000)
