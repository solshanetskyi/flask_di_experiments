from flask_restful import Resource
from injector import inject

from flask_.services import PaymentOptionsService


class CreditCardResource(Resource):
    @inject
    def __init__(self, service_: PaymentOptionsService):
        self.service = service_
        print("dupple pusssto")

    def get(self):
        return {
            "credit-card": "Bomgara!!!--" + self.service.get_data()
        }
