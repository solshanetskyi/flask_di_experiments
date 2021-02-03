from flask_injector import RequestScope
from injector import SingletonScope, NoScope

from flask_.services import Repository, MySqlRepository, InMemoryRepository
from flask_.services_evolve import EvolveClient, EvolveClientLive


def configure_(binder):
    binder.bind(Repository, to=MySqlRepository)

    # binder.bind(EvolveClient, to=EvolveClientLive, scope=NoScope)
    # binder.bind(EvolveClient, to=EvolveClientLive, scope=RequestScope)
    binder.bind(EvolveClient, to=EvolveClientLive, scope=SingletonScope)
