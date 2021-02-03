from example_01.analyser import FreshBookersAnalyser

analyser = FreshBookersAnalyser()

analyzed_freshbookers = analyser.get_top_freshbookers()

for freshbooker in analyzed_freshbookers:
    print(freshbooker)
