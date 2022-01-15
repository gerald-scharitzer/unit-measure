from unitsofmeasure import binprefix

def test_it():
    items = binprefix.si_binary_prefixes.items()
    assert len(items) == 8 # there are 8 binary prefixes

    for (key, prefix) in items:
        print(key, prefix)
        assert key == prefix.symbol
