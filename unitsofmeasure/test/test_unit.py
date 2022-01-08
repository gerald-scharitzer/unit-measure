"""Test Unit"""
import pytest
from unitsofmeasure import Dimension, no_prefix, no_unit, Prefix, scalar, Unit
from unitsofmeasure.decprefix import DecimalPrefixes

# TODO test fraction
@pytest.mark.parametrize(
    "symbol , name       , dimension        , prefix"          ,[
    ("%"    , "percent"  , Dimension()      , no_prefix        ), # scalar
    ("kg"   , "kilogram" , Dimension(kg=1)  , DecimalPrefixes.k), # SI base units
    ("m"    , "metre"    , Dimension(m=1)   , no_prefix        ),
    ("s"    , "second"   , Dimension(s=1)   , no_prefix        ),
    ("A"    , "ampere"   , Dimension(A=1)   , no_prefix        ),
    ("K"    , "kelvin"   , Dimension(K=1)   , no_prefix        ),
    ("cd"   , "candela"  , Dimension(cd=1)  , no_prefix        ),
    ("mol"  , "mole"     , Dimension(mol=1) , no_prefix        )
])
def test_unit(symbol: str, name: str, dimension: Dimension, prefix: Prefix) -> None:
    unit = Unit(symbol=symbol, name=name, dimension=dimension, prefix=prefix)
    assert unit.symbol    == symbol
    assert unit.name      == name
    assert unit.dimension == dimension
    assert unit.prefix    == prefix

def test_no_unit() -> None:
    assert no_unit.symbol    == ""
    assert no_unit.name      == ""
    assert no_unit.dimension == scalar
    assert no_unit.prefix    == no_prefix
