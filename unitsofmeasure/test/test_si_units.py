"""Test SI Units"""
from unitsofmeasure import base, derived

def test_it() -> None:
    units = base.si_base_units | derived.si_derived_units
    for (key, unit) in units.items():
        print(key, unit, unit.name)
        if (key == "degC"):
            assert unit.symbol == "°C"
        else:
            assert key == unit.symbol
