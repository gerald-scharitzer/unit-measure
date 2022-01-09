"""Test Unit"""
from unitsofmeasure.base import SiBaseUnits
from unitsofmeasure.derived import SiDerivedUnits

def test_it() -> None:
    units = SiBaseUnits.get_units() | SiDerivedUnits.get_units()
    for (key, unit) in units.items():
        print(key, unit, unit.name)
        if (key == "degC"):
            assert unit.symbol == "°C"
        else:
            assert key == unit.symbol
