from users import Users


users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {user.username: user for user in users}

userid_mapping = {user.id: user for user in users} 

def authentication(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):      # 'payload' is the contents of the JWT token
    user_id = payload['idendity']
    return userid_mapping.get(user_id, None)
