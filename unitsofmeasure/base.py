from unitsofmeasure import Dimension, Unit, UnitClass
from unitsofmeasure.decprefix import DecimalPrefixes

class SiBaseUnits(UnitClass):
    """SI Base Units"""

    kg  = Unit("kg", "kilogram", Dimension(kg=1), DecimalPrefixes.k)
    m   = Unit("m", "metre", Dimension(m=1))
    s   = Unit("s", "second", Dimension(s=1))
    A   = Unit("A", "ampere", Dimension(A=1))
    K   = Unit("K", "kelvin", Dimension(K=1))
    cd  = Unit("cd", "candela", Dimension(cd=1))
    mol = Unit("mol", "mole", Dimension(mol=1))

    @classmethod
    def get_units(cls) -> dict[str, Unit]:
        return {
            "kg":  cls.kg,
            "m":   cls.m,
            "s":   cls.s,
            "A":   cls.A,
            "K":   cls.K,
            "cd":  cls.cd,
            "mol": cls.mol
        }
