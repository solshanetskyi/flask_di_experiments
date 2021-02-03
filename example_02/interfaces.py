from abc import ABC, abstractmethod


class FreshBookersProvider(ABC):

    @abstractmethod
    def get_freshbookers(self):
        pass
