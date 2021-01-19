from abc import ABC, abstractmethod

from injector import inject


class Repository(ABC):
    @abstractmethod
    def get_data(self):
        pass


class MySqlRepository(Repository):

    def get_data(self) -> str:
        return "getting data from MYSQLLLLL"


class InMemoryRepository(Repository):

    def get_data(self) -> str:
        return "getting data from Memoryyyyy"


class MyService:
    @inject
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_content(self):
        return self.repository.get_data()
