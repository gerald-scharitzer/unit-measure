from unitsofmeasure import base

def test_it():
    items = base.si_base_units.items()
    assert len(items) == 7 # there are 7 base units

    for (key, unit) in items:
        print(key, unit, unit.name)
        assert key == unit.symbol
