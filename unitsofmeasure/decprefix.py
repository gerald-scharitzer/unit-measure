from unitsofmeasure import Prefix, PrefixClass

class DecimalPrefixes(PrefixClass):
    """Decimal (SI) Prefixes"""
    da = Prefix(10,   1, "da", "deca")
    h  = Prefix(10,   2, "h",  "hecto")
    k  = Prefix(10,   3, "k",  "kilo")
    M  = Prefix(10,   6, "M",  "mega")
    G  = Prefix(10,   9, "G",  "giga")
    T  = Prefix(10,  12, "T",  "tera")
    P  = Prefix(10,  15, "P",  "peta")
    E  = Prefix(10,  18, "E",  "exa")
    Z  = Prefix(10,  21, "Z",  "zetta")
    Y  = Prefix(10,  24, "Y",  "yotta")
    d  = Prefix(10,  -1, "d",  "deci")
    c  = Prefix(10,  -2, "c",  "centi")
    m  = Prefix(10,  -3, "m",  "milli")
    µ  = Prefix(10,  -6, "µ",  "micro")
    n  = Prefix(10,  -9, "n",  "nano")
    p  = Prefix(10, -12, "p",  "pico")
    f  = Prefix(10, -15, "f",  "femto")
    a  = Prefix(10, -18, "a",  "atto")
    z  = Prefix(10, -21, "z",  "zepto")
    y  = Prefix(10, -24, "y",  "yocto")

    @classmethod
    def get_prefixes(cls) -> dict[str, Prefix]:
        return {
            "da": cls.da,
            "h" : cls.h,
            "k" : cls.k,
            "M" : cls.M,
            "G" : cls.G,
            "T" : cls.T,
            "P" : cls.P,
            "E" : cls.E,
            "Z" : cls.Z,
            "Y" : cls.Y,
            "d" : cls.d,
            "c" : cls.c,
            "m" : cls.m,
            "µ" : cls.µ,
            "n" : cls.n,
            "p" : cls.p,
            "f" : cls.f,
            "a" : cls.a,
            "z" : cls.z,
            "y" : cls.y
        }
