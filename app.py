import os

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
import re

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

#uri = os.getenv("DATABASE_URL")  # or other relevant config var
##    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_1', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'henry'
api = Api(app)

#aapp.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/items/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug = True)
