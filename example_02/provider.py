# FreshBookersProvider <- CsvFreshBookersProvider
from example_02.interfaces import FreshBookersProvider
from example_02.model import FreshBooker


class CsvFreshBookersProvider(FreshBookersProvider):
    def __init__(self, file_name):
        self._file_name = file_name

    def get_freshbookers(self):
        freshbookers = list()

        with open(self._file_name) as log_file:
            freshbookers_text = log_file.readlines()

            for line in freshbookers_text:
                first_name, last_name = line.split(" ")
                freshbookers.append(FreshBooker(first_name.strip(), last_name.strip()))

        return freshbookers
