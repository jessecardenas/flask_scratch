#!python3
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.FlaskConfig')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run() # this will run a web server on port 5000
    # print(hello_world())




