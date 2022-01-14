from unitsofmeasure import derived

def test_it():
    items = derived.si_derived_units.items()
    assert len(items) == 22 # there are 22 derived units

    for (key, unit) in items:
        print(key, unit, unit.name)
        if (key == "degC"):
            assert unit.symbol == "°C"
        else:
            assert key == unit.symbol
