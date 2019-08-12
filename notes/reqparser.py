from flask_restful import Resource, Api, reqparser

def put(self, name):
    #data = request.get_json()
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    data = parser.parse_args()

