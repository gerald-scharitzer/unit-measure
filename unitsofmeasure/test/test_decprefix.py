from unitsofmeasure import decprefix

def test_it():
    items = decprefix.si_decimal_prefixes.items()
    assert len(items) == 20 # there are 20 decimal prefixes

    for (key, prefix) in items:
        print(key, prefix)
        assert key == prefix.symbol
