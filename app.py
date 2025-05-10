#!python3
from flask import Flask, session, request, render_template
from functools import wraps
from utils import auth
import config as cfg

app = Flask(__name__, template_folder='resources/templates', static_folder='resources/static')
app.config.from_object('config.FlaskConfig')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def auth_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if auth.check_auth(username, password, auth_source=cfg.auth_source):
            session.clear()
            session['username'] = username
            session.permanent = True
            return 'Login success\n', 200
        else:
            return 'Invalid username or password\n', 401
    # check login status
    if 'username' in session:
        return 'Logged in as {}\n'.format(session['username'])
    else:
        return 'Not logged in. I dont know you!\n'

@app.route('/auth/logout')
def auth_logout():
    # session.pop('username', None)
    session.clear()
    return 'Logout successful\n'

def require_login(function):
    @wraps(function)
    def inner():
        if 'username' not in session:
            return 'Login required\n', 403
        return function()
    return inner

@app.route("/protected")
@require_login
def protected():
    return "<p>Secret area!</p>\n"


if __name__ == "__main__":
    app.run() # this will run a web server on port 5000
    # print(hello_world())


