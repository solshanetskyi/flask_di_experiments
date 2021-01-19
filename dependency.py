from injector import singleton

from services import MyService, Repository, MySqlRepository, InMemoryRepository


def configure_(binder):
    binder.bind(Repository, to=InMemoryRepository, scope=singleton)
