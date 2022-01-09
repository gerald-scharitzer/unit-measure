from unitsofmeasure.base import SiBaseUnits

def test_it():
    items = SiBaseUnits.get_units().items()
    assert len(items) == 7 # there are 7 base units

    for (key, unit) in items:
        print(key, unit, unit.name)
        assert key == unit.symbol
