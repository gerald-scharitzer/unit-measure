"""Test UnitMap"""
from unitsofmeasure import Unit, UnitMap

def test_it() -> None:
    # not all objects are weakly referencable, but class instances are
    # https://docs.python.org/3/library/weakref.html
    class Measure:
        def __init__(self, value: object) -> None:
            self.value = value
    measure = Measure(10)
    b = Unit("b", "bit")
    units = UnitMap()
    units.map_to_unit(measure, b)
    unit = units.get_unit_of(measure)
    assert unit == b
