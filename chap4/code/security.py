users = [
    {
        'id': 1,
        'username': 'bob'
        'password': 'asdf'
    }
]

username_mapping = {
    'bob': {
        'id': 1,
        'username': 'bob'
        'password': 'asdf'
    }
}

userid_mapping = {
    1: {
        'id': 1,
        'username': 'bob'
        'password': 'asdf'
    }
} 


def authentication(username, password):
    user = username_mapping.get(username, None)
    if user and user['password'] == password:
        return user

def identity(payload):      # 'payload' is the contents of the JWT token
    user_id = payload['idendity']
    return userid_mapping.get(user_id, None)
