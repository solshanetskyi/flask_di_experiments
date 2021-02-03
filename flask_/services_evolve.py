import uuid
from abc import ABC, abstractmethod

from injector import inject


class EvolveClient(ABC):

    @abstractmethod
    def get_something(self):
        pass


class EvolveClientLive(EvolveClient):
    def __init__(self):
        self.id = uuid.uuid4()

    def get_something(self):
        return self.id


class ThirdLevelService:
    @inject
    def __init__(self, evolve_client: EvolveClient):
        self.evolve_client = evolve_client

    def get_data(self, response: dict):
        response["third_service"] = f"I have evolve instance with id: {self.evolve_client.get_something()}"
        return


class SecondLevelService:
    @inject
    def __init__(self, third_level_service: ThirdLevelService):
        self.third_level_service = third_level_service

    def get_data(self, response: dict):
        response["second_service"] = "I don't have evolve instance!"

        self.third_level_service.get_data(response)
        return response


class FirstLevelService:
    @inject
    def __init__(self, second_level_service: SecondLevelService, evolve_client: EvolveClient):
        self.second_level_service = second_level_service
        self.evolve_client = evolve_client

    def get_data(self):
        response = {
            "first_service": f"I have evolve instance with id: {self.evolve_client.get_something()}"
        }

        self.second_level_service.get_data(response)

        return response
