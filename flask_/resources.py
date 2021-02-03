from flask_restful import Resource
from injector import inject

from flask_.services import PaymentOptionsService
from flask_.services_evolve import FirstLevelService


class PaymentOptionsResource(Resource):
    @inject
    def __init__(self, service: PaymentOptionsService):
        self.service = service

    def get(self):
        return {
            "payment-options": "Lenin! Partiya! " + self.service.get_payment_options()
        }


class EvolveExampleResource(Resource):
    @inject
    def __init__(self, service: FirstLevelService):
        self.service = service

    def get(self):
        return self.service.get_data()

