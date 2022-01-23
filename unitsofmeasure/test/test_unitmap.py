"""Test UnitMap"""
from unitsofmeasure import map_to_unit, Unit, UnitMap

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

def test_decorator() -> None:
    units = UnitMap()
    b = Unit("b", "bit")

    @map_to_unit(units, b)
    def func() -> int:
        return 10

    unit = units.get_unit_of(func)
    assert unit == b
