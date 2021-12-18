from unitsofmeasure.derived import SiDerivedUnits

def test_it():
    items = SiDerivedUnits.get_units().items()
    assert len(items) == 22 # there are 22 derived units

    for (key, unit) in items:
        print(key, unit)
        if (key == "degC"):
            assert unit.symbol == "°C"
        else:
            assert key == unit.symbol
