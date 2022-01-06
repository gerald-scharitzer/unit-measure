from unitsofmeasure import Dimension, no_prefix, Unit, UnitClass
from unitsofmeasure.decprefix import DecimalPrefixes

class SiBaseUnits(UnitClass):
    """SI Base Units"""

    kg  = Unit(Dimension(kg=1), DecimalPrefixes.k, "kg", "kilogram")
    m   = Unit(Dimension(m=1), no_prefix, "m", "metre")
    s   = Unit(Dimension(s=1), no_prefix, "s", "second")
    A   = Unit(Dimension(A=1), no_prefix, "A", "ampere")
    K   = Unit(Dimension(K=1), no_prefix, "K", "kelvin")
    cd  = Unit(Dimension(cd=1), no_prefix, "cd", "candela")
    mol = Unit(Dimension(mol=1), no_prefix, "mol", "mole")

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
