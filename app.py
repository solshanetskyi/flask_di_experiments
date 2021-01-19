from abc import ABC, abstractmethod

from flask import Flask
from flask_injector import FlaskInjector
from injector import singleton

from dependency import configure_
from services import MyService

app = Flask(__name__)


@app.route('/')
def hello_world(service: MyService):
    return service.get_content()


FlaskInjector(app=app, modules=[configure_])

if __name__ == '__main__':
    app.run()
