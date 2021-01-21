import uuid
from abc import ABC

from injector import InstanceProvider, Module, provider, Injector, ClassProvider, SingletonScope

from injector import inject

from inject_.domain import UserManager, UserModule, UserAttributeModule

injector = Injector([UserModule, UserAttributeModule])

user_manager_1 = injector.get(UserManager)
print(user_manager_1.user.id)

user_manager_2 = injector.get(UserManager)
print(user_manager_2.user.id)

user_manager_2.risk_it()
