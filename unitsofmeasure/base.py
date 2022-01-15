"""SI Base Units"""
from unitsofmeasure import Dimension, Unit
from unitsofmeasure import decprefix

kg  = Unit("kg", "kilogram", Dimension(kg=1), decprefix.k)
m   = Unit("m", "metre", Dimension(m=1))
s   = Unit("s", "second", Dimension(s=1))
A   = Unit("A", "ampere", Dimension(A=1))
K   = Unit("K", "kelvin", Dimension(K=1))
cd  = Unit("cd", "candela", Dimension(cd=1))
mol = Unit("mol", "mole", Dimension(mol=1))

# map symbols to units
si_base_units: dict[str, Unit] = {
    "kg":  kg,
    "m":   m,
    "s":   s,
    "A":   A,
    "K":   K,
    "cd":  cd,
    "mol": mol
}
