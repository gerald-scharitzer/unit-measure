from unitsofmeasure import Dimension, Unit, UnitClass

class SiDerivedUnits(UnitClass):
    """SI Derived Units

    The symbol of unit ohm is Ω (Unicode OHM SIGN).
    You can map this to other identifiers by assignment (e.g. `ohm = Ω`).

    The symbol of unit degree Celsius is °C, but that is not a valid Python identifier.
    Therefore it is mapped to degC.
    """
    rad  = Unit(Dimension(), 0, "rad", "radian")
    sr   = Unit(Dimension(), 0, "sr", "steradian")
    Hz   = Unit(Dimension(s=-1), 0, "Hz", "hertz")
    N    = Unit(Dimension(kg=1, m=1, s=-2), 0, "N", "newton")
    Pa   = Unit(Dimension(kg=1, m=-1, s=-2), 0, "Pa", "pascal")
    J    = Unit(Dimension(kg=1, m=2, s=-2), 0, "J", "joule")
    W    = Unit(Dimension(kg=1, m=2, s=-3), 0, "W", "watt")
    C    = Unit(Dimension(A=1, s=1), 0, "C", "coulomb")
    V    = Unit(Dimension(kg=1, m=2, s=-3, A=-1), 0, "V", "volt")
    F    = Unit(Dimension(kg=-1, m=-2, s=4, A=2), 0, "F", "farad")
    Ω    = Unit(Dimension(kg=1, m=2, s=-3, A=-2), 0, "Ω", "ohm")
    S    = Unit(Dimension(kg=-1, m=-2, s=3, A=2), 0, "S", "siemens")
    Wb   = Unit(Dimension(kg=1, m=2, s=-2, A=-1), 0, "Wb", "weber")
    T    = Unit(Dimension(kg=1, s=-2, A=-1), 0, "T", "tesla")
    H    = Unit(Dimension(kg=1, m=2, s=-2, A=-2), 0, "H", "henry")
    degC = Unit(Dimension(K=1), 0, "°C", "degree Celsius")
    lm   = Unit(Dimension(cd=1), 0, "lm", "lumen")
    lx   = Unit(Dimension(cd=1, m=2), 0, "lx", "lux")
    Bq   = Unit(Dimension(s=-1), 0, "Bq", "becquerel")
    Gy   = Unit(Dimension(m=2, s=-2), 0, "Gy", "gray")
    Sv   = Unit(Dimension(m=2, s=-2), 0, "Sv", "sievert")
    kat  = Unit(Dimension(mol=1, s=-1), 0, "kat", "katal")

    @classmethod
    def get_units(cls) -> dict[str, Unit]:
        return {
            "rad":  cls.rad,
            "sr":   cls.sr,
            "Hz":   cls.Hz,
            "N":    cls.N,
            "Pa":   cls.Pa,
            "J":    cls.J,
            "W":    cls.W,
            "C":    cls.C,
            "V":    cls.V,
            "F":    cls.F,
            "Ω":    cls.Ω,
            "S":    cls.S,
            "Wb":   cls.Wb,
            "T":    cls.T,
            "H":    cls.H,
            "degC": cls.degC, # TODO map degC and/or °C?
            "lm":   cls.lm,
            "lx":   cls.lx,
            "Bq":   cls.Bq,
            "Gy":   cls.Gy,
            "Sv":   cls.Sv,
            "kat":  cls.kat
        }
