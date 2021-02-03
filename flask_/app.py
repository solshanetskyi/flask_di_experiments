from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api

from flask_.dependency import configure_
from flask_.resources import PaymentOptionsResource, EvolveExampleResource


def create_app():
    app = Flask(__name__)

    api = Api(app)

    api.add_resource(PaymentOptionsResource, "/")
    api.add_resource(EvolveExampleResource, "/evolve")

    FlaskInjector(app=app, modules=[configure_])

    return app
