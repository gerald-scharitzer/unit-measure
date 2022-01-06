from unitsofmeasure.decprefix import DecimalPrefixes

def test_it():
    items = DecimalPrefixes.get_prefixes().items()
    assert len(items) == 20 # there are 20 decimal prefixes

    for (key, prefix) in items:
        print(key, prefix)
        assert key == prefix.symbol
