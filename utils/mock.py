from werkzeug.security import generate_password_hash, check_password_hash

# mock databases
user_db = {'bob': {'password': generate_password_hash('secret')}, 'kate': {'password': generate_password_hash('supersecret')} }

def check_auth(usr, pwd):
    user = user_db.get(usr)
    if user and check_password_hash(user['password'], pwd):
        return True
    return False


