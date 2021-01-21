from injector import singleton

from flask_.services import Repository, MySqlRepository


def configure_(binder):
    binder.bind(Repository, to=MySqlRepository, scope=singleton)
