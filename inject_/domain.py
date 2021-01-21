import uuid
from abc import ABC

from injector import inject, provider, ClassProvider, Module, SingletonScope, InstanceProvider


class Name:
    pass


class Description:
    pass


class User(ABC):
    @inject
    def __init__(self, name: Name, description: Description):
        self.name = name
        self.description = description


class SuperUser(User):
    @inject
    def __init__(self, name: Name, description: Description):
        super().__init__(name, description)
        self.id = "super"


class LoserUser(User):
    @inject
    def __init__(self, name: Name, description: Description):
        super().__init__(name, description)
        self.id = "loser" + str(uuid.uuid4())


class UserManager:
    @inject
    def __init__(self, user_to_manage: User):
        self.user = user_to_manage

    def risk_it(self):
        do_stuff(self.user)


class UserModule(Module):
    def configure(self, binder):
        binder.bind(User, to=ClassProvider(LoserUser), scope=SingletonScope)
        pass


class UserAttributeModule(Module):

    def callable_stuff(self):
        return 'Name is name...'

    def configure(self, binder):
        binder.bind(Name, to=self.callable_stuff, scope=SingletonScope)

    @provider
    def describe(self, name: Name) -> Description:
        return f'{name} is a man of astounding insight'


@inject
def do_stuff(user: User):
    print("Uhi!!!")
    print(user.name)
