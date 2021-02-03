from example_02.analyser import FreshBookersAnalyser
from example_02.provider import CsvFreshBookersProvider

freshbookers_provider = CsvFreshBookersProvider("freshbookers.txt")
analyser = FreshBookersAnalyser(freshbookers_provider)

analyzed_freshbookers = analyser.get_top_freshbookers()

for freshbooker in analyzed_freshbookers:
    print(freshbooker)

# Inversion of Control (IoC) means that objects do not create other objects on which they rely to do their work.
# Instead, they get the objects that they need from an outside source

# Dependency Injection (DI) means that this is done without the object intervention,
# usually by a framework component that passes constructor parameters
