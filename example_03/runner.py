from injector import Injector

from example_03.analyser import FreshBookersAnalyser
from example_03.interfaces import FreshBookersProvider
from example_03.provider import CsvFreshBookersProvider


def configure(binder):
    binder.bind(FreshBookersProvider, to=CsvFreshBookersProvider("freshbookers.txt"))


injector = Injector(configure)

analyser = injector.get(FreshBookersAnalyser)

analyzed_freshbookers = analyser.get_top_freshbookers()

for freshbooker in analyzed_freshbookers:
    print(freshbooker)
