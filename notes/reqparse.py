from flask_restful import Resource, Api, reqparse

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )


def put(self, name):
    #data = request.get_json()
    data = Item.parser.parse_args()     # use the class method

