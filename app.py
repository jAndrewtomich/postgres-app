import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import PGapp

@app.route('/')
def hello():
    secret_key = app.config.get("SECRET_KEY") 
    return f"The skey is {secret_key}"


@app.route('/<name>')
def hello_name(name):
    return "Hello, {}!".format(name)


if __name__ == '__main__':
    app.run()

