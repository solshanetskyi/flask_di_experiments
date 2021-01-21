from flask_restful import Resource
from injector import inject

from flask_.services import PaymentOptionsService


class CreditCardResource(Resource):
    @inject
    def __init__(self, service: PaymentOptionsService):
        self.service = service

    def get(self):
        return {
            "credit-card": "Bomgara!!!--" + self.service.get_data()
        }
