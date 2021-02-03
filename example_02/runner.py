from example_02.analyser import FreshBookersAnalyser
from example_02.provider import CsvFreshBookersProvider

freshbookers_provider = CsvFreshBookersProvider("freshbookers.txt")
analyser = FreshBookersAnalyser(freshbookers_provider)

analyzed_freshbookers = analyser.get_top_freshbookers()

for freshbooker in analyzed_freshbookers:
    print(freshbooker)
