"""Test Dimension"""
import pytest
from unitsofmeasure import Dimension, SCALAR

@pytest.mark.parametrize(
    "dimension                    , kg , m , s , A , K , cd , mol , symbol , representation",[
    (Dimension()                  ,  0 , 0 , 0 , 0 , 0 ,  0 ,   0 , ""     , "Dimension(kg=0, m=0, s=0, A=0, K=0, cd=0, mol=0)"), # scalar
    (Dimension(kg=1, symbol="m")  ,  1 , 0 , 0 , 0 , 0 ,  0 ,   0 , "m"    , "Dimension(kg=1, m=0, s=0, A=0, K=0, cd=0, mol=0)"), # SI base units
    (Dimension(m=1, symbol="l")   ,  0 , 1 , 0 , 0 , 0 ,  0 ,   0 , "l"    , "Dimension(kg=0, m=1, s=0, A=0, K=0, cd=0, mol=0)"),
    (Dimension(s=1, symbol="t")   ,  0 , 0 , 1 , 0 , 0 ,  0 ,   0 , "t"    , "Dimension(kg=0, m=0, s=1, A=0, K=0, cd=0, mol=0)"),
    (Dimension(A=1, symbol="I")   ,  0 , 0 , 0 , 1 , 0 ,  0 ,   0 , "I"    , "Dimension(kg=0, m=0, s=0, A=1, K=0, cd=0, mol=0)"),
    (Dimension(K=1, symbol="T")   ,  0 , 0 , 0 , 0 , 1 ,  0 ,   0 , "T"    , "Dimension(kg=0, m=0, s=0, A=0, K=1, cd=0, mol=0)"),
    (Dimension(cd=1, symbol="Iv") ,  0 , 0 , 0 , 0 , 0 ,  1 ,   0 , "Iv"   , "Dimension(kg=0, m=0, s=0, A=0, K=0, cd=1, mol=0)"),
    (Dimension(mol=1, symbol="n") ,  0 , 0 , 0 , 0 , 0 ,  0 ,   1 , "n"    , "Dimension(kg=0, m=0, s=0, A=0, K=0, cd=0, mol=1)")
])
def test(dimension: Dimension, kg: int, m: int, s: int, A: int, K: int, cd: int, mol: int, symbol: str, representation: str) -> None:
    assert dimension.kg == kg
    assert dimension.m == m
    assert dimension.s == s
    assert dimension.A == A
    assert dimension.K == K
    assert dimension.cd == cd
    assert dimension.mol == mol
    assert dimension.symbol == symbol

    # test equality
    other = Dimension(kg, m, s, A, K, cd, mol)
    assert id(dimension) != id(other)
    assert dimension == other

    # test string
    assert str(dimension) == symbol

    # test representation
    assert repr(dimension) == representation

@pytest.mark.parametrize(
    "kg  , m   , s   , A   , K   , cd  , mol",[
    (0.5 , 0   , 0   , 0   , 0   , 0   , 0  ),
    (0   , 0.5 , 0   , 0   , 0   , 0   , 0  ),
    (0   , 0   , 0.5 , 0   , 0   , 0   , 0  ),
    (0   , 0   , 0   , 0.5 , 0   , 0   , 0  ),
    (0   , 0   , 0   , 0   , 0.5 , 0   , 0  ),
    (0   , 0   , 0   , 0   , 0   , 0.5 , 0  ),
    (0   , 0   , 0   , 0   , 0   , 0   , 0.5),
    ("1" , 0   , 0   , 0   , 0   , 0   , 0  ),
    (0   , "1" , 0   , 0   , 0   , 0   , 0  ),
    (0   , 0   , "1" , 0   , 0   , 0   , 0  ),
    (0   , 0   , 0   , "1" , 0   , 0   , 0  ),
    (0   , 0   , 0   , 0   , "1" , 0   , 0  ),
    (0   , 0   , 0   , 0   , 0   , "1" , 0  ),
    (0   , 0   , 0   , 0   , 0   , 0   , "1")
])
def test_exceptions(kg: int, m: int, s: int, A: int, K: int, cd: int, mol: int) -> None:
    with pytest.raises(TypeError, match="^The exponent must be an integer.$"):
        Dimension(kg, m, s, A, K, cd, mol)

def test_scalar() -> None:
    assert SCALAR.kg  == 0
    assert SCALAR.m   == 0
    assert SCALAR.s   == 0
    assert SCALAR.A   == 0
    assert SCALAR.K   == 0
    assert SCALAR.cd  == 0
    assert SCALAR.mol == 0
