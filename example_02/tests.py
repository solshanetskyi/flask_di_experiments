from example_02.analyser import FreshBookersAnalyser
from example_02.interfaces import FreshBookersProvider
from example_02.model import FreshBooker


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


def test_analyser_brings_ii_to_the_bottom():
    freshbookers_provider = FreshBookersProviderMock()
    analyser = FreshBookersAnalyser(freshbookers_provider)

    analyzed_freshbookers = analyser.get_top_freshbookers()

    assert analyzed_freshbookers[-1].first_name == "Dharmesh"
