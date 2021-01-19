from flask_restful import Resource
from injector import inject

from services import MyService


class CreditCardResource(Resource):
    @inject
    def __init__(self, service: MyService):
        self.service = service

    def get(self):
        return {
            "credit-card": "Bomgara!!!--" + self.service.get_content()
        }
