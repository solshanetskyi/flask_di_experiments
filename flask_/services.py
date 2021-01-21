from abc import ABC, abstractmethod

from injector import inject


class Repository(ABC):
    @abstractmethod
    def get_data(self):
        pass


class MySqlRepository(Repository):

    def get_data(self) -> str:
        return "Content retrieved from MYSQLLLLL database"


class InMemoryRepository(Repository):

    def get_data(self) -> str:
        return "Content retrieved from InMemory database"


class PaymentOptionsService:
    @inject
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_data(self):
        return self.repository.get_data()


class PaymentService:
    @inject
    def __init__(self, payment_options_service: PaymentOptionsService):
        self.payment_options_service = payment_options_service

    def pay(self):
        return self.payment_options_service.get_data()
