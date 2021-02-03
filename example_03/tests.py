from injector import Injector

from example_03.analyser import FreshBookersAnalyser
from example_03.interfaces import FreshBookersProvider
from example_03.model import FreshBooker


class FreshBookersProviderMock(FreshBookersProvider):

    def get_freshbookers(self):
        return [
            FreshBooker("Dharmesh", "Dhakan"),
            FreshBooker("Dharmesh", "Dhakan"),
            FreshBooker("Dharmesh", "Dhakan"),
            FreshBooker("Sergii", "Olshanetksyi"),
            FreshBooker("Dharmesh", "Dhakan"),
            FreshBooker("Dharmesh", "Dhakan"),
            FreshBooker("Dharmesh", "Dhakan"),
        ]


def configure(binder):
    binder.bind(FreshBookersProvider, to=FreshBookersProviderMock)


def test_analyser_brings_ii_to_the_bottom():
    injector = Injector(configure)

    analyser = injector.get(FreshBookersAnalyser)

    analyzed_freshbookers = analyser.get_top_freshbookers()

    assert analyzed_freshbookers[-1].first_name == "Sergii"
