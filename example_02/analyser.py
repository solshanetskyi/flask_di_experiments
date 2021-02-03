import random

from example_02.interfaces import FreshBookersProvider


# FreshBookersProvider <- CsvFreshBookersProvider
class FreshBookersAnalyser:
    def __init__(self, freshbookers_provider: FreshBookersProvider):
        self._freshbookers_provider = freshbookers_provider

    def get_top_freshbookers(self):
        freshbookers = self._freshbookers_provider.get_freshbookers()

        random.shuffle(freshbookers)

        indices_of_bad_freshbookers = [index for index, freshbooker in enumerate(freshbookers)
                                       if "ii" in freshbooker.first_name]

        for index in indices_of_bad_freshbookers:
            freshbookers.append(freshbookers.pop(index))

        return freshbookers[:10]
