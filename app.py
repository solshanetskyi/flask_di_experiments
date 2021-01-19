from abc import ABC, abstractmethod

from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api
from injector import singleton

from dependency import configure_
from resources import CreditCardResource
from services import MyService

app = Flask(__name__)


@app.route('/')
def hello_world(service: MyService):
    return service.get_content()


api = Api(app)
api.add_resource(CreditCardResource, "/credit_card")

FlaskInjector(app=app, modules=[configure_])

if __name__ == '__main__':
    app.run()
