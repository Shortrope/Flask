from flask import Flask, jsonify, request

app = Flask(__name__)

# store is a dictionary - name:, items: []
# items is a list of dictionaries - name:, price:
stores = [
    {
        'name': 'Maks',
        'items': [
            {
                'name': 'Chair',
                'price': 12.95
            }
        ]
    },
    {
        'name': 'Kams',
        'items': [
            {
                'name': 'Rope',
                'price': 145.95
            }
        ]
    }

]


@app.route('/')
def home():
    return "Hey Buddy!"

# GET /store
@app.route('/store')
def get_stores():
    if stores:
        return jsonify({'stores': stores})
    else:
        return "<h1>We have no stores!</h1>"

# GET /store/<string:name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/name'
def get_store(name):
    for store in stores:
        if store['name'].lower() == name.lower():
            return jsonify(store)
    return jsonify({'message': "No store named '{}'.".format(name)})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'].lower() == name.lower():
            if store['items']:
                return jsonify({'items': store['items']})
            else:
                return jsonify({'message': "No items in {} store!".format(name)})
    return jsonify({'message': "No store named '{}'.".format(name)})
    
# POST /store data: {name:}  - Create new store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    req_data = request.get_json()
    new_item = {
            'name': req_data['name'],
            'price': req_data['price']
    }
    for store in stores:
        if store['name'].lower() == name.lower():
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': "No store named '{}'.".format(name)})






app.run(host='0.0.0.0', port=5000)
