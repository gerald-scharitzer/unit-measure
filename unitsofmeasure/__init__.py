"""Units of Measure - based on the International System of Units - 9th edition

https://www.bipm.org/en/publications/si-brochure
"""
from fractions import Fraction
from weakref import ref

# TODO map dimensions to quantity names
class Dimension:
    """Dimension of quantity: a product of integer powers of SI base units
    
    For each SI base unit symbol (kg, m, s, A, K, cd, mol) an attribute with the same name stores the exponent.
    """

    def __init__(
            self,
            kg:  int = 0,
            m:   int = 0,
            s:   int = 0,
            A:   int = 0,
            K:   int = 0,
            cd:  int = 0,
            mol: int = 0
        ) -> None:
        """The default dimension is the scalar, where all exponents are 0.

        Thus the product is 1, the identity element of dimensions."""
        self.kg  = kg
        self.m   = m
        self.s   = s
        self.A   = A
        self.K   = K
        self.cd  = cd
        self.mol = mol
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return NotImplemented
        return (
            self.kg  == other.kg and
            self.m   == other.m  and
            self.s   == other.s  and
            self.A   == other.A  and
            self.K   == other.K  and
            self.cd  == other.cd and
            self.mol == other.mol
        )
    
    def __repr__(self) -> str:
        return (self.__class__.__name__ +
            "(kg="   + repr(self.kg)  +
            ", m="   + repr(self.m)   +
            ", s="   + repr(self.s)   +
            ", A="   + repr(self.A)   +
            ", K="   + repr(self.K)   +
            ", cd="  + repr(self.cd)  +
            ", mol=" + repr(self.mol) +
            ")")

# The identity element of dimensions
scalar = Dimension()

class Prefix:
    """A number to scale units in orders of magnitude.
    
    Each prefix has an integer base and exponent.
    The base is the magnitude and the exponent is the number of orders.
    """

    def __init__(
            self,
            base: int = 10,
            exponent: int = 0,
            symbol: str = "",
            name: str = ""
        ) -> None:
        """The default is 10 raised to 0, resulting in the value 1"""
        self.base = base
        self.exponent = exponent
        self.symbol = symbol
        self.name = name
    
    def __eq__(self, other) -> bool:
        """Exponent zero with different bases is not equal, because the same non-zero exponent results in different values."""
        if type(self) != type(other):
            return NotImplemented
        return (
            self.base     == other.base and
            self.exponent == other.exponent
        )

    def __str__(self) -> str:
        return self.symbol
    
    def __repr__(self) -> str:
        return (self.__class__.__name__ +
            "(base=" + repr(self.base) +
            ", exponent=" + repr(self.exponent) +
            ", symbol=\"" + self.symbol +
            "\", name=\"" + self.name +
            "\")")

# No prefix or the prefix of 1
no_prefix = Prefix()

class Unit:
    """A Unit has a Dimension.

    Scalars are the identity element, which is the default dimension.
    Units have a symbol: a short string used in formulas, tables, and charts.
    Units have a prefix, which specifies the order of magnitude.
    Prefixes with base 10 and exponents that are integer multiples of 3 in the interval [-24,24] map to SI prefixes.
    """

    _one = Fraction(1,1)

    def __init__(
            self,
            symbol: str = "",
            name: str = "",
            dimension: Dimension = scalar,
            prefix: Prefix = no_prefix, # none = one
            factor: Fraction = _one
        ) -> None:
        self.symbol = symbol
        self.name = name
        self.dimension = dimension
        self.prefix = prefix
        self.factor = factor
    
    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            return NotImplemented
        return (
            self.symbol    == other.symbol    and
            self.name      == other.name      and
            self.dimension == other.dimension and
            self.prefix    == other.prefix    and
            self.factor    == other.factor
        )
    
    def __str__(self) -> str:
        return self.symbol
    
    def __repr__(self) -> str:
        return (self.__class__.__name__ +
            "(symbol=\"" + self.symbol +
            "\", name=\"" + self.name +
            "\", dimension=" + repr(self.dimension) +
            ", prefix=" + repr(self.prefix) +
            ", factor=" + repr(self.factor) +
            ")")

# No unit or the unit of 1
no_unit = Unit()

class GarbageError(Exception):
    pass

class UnitMap:
    """Map objects to their units.

    The objects are not used as keys directly, because not all objects are hashable.
    Instead the integer value of id(object) is used as key,
    but two objects with non-overlapping lifetimes may have the same id() value.
    See https://docs.python.org/3/library/functions.html#id.
    The units can be objects as well and need not be of type Unit.
    """

    def __init__(self) -> None:
        self.units = {} # dictionary maps id(object) to (ref(object), unit)
    
    def map_to_unit(self, o: object, unit: object) -> None:
        """Map the object ID to the tuple (object, unit) to keep a reference to the object.

        Otherwise the object could be garbage collected and its ID re-used for a different object.
        TODO Remove the object ID from the dictionary on finalize.
        """
        self.units[id(o)] = (ref(o), unit)

    def get_unit_of(self, o: object) -> object:
        """Return the unit mapped to the object.
        
        Throws GarbageError when to object was garbage-collected already.
        """

        # map the object ID to its tuple (ref, unit) and then return the unit
        (weak, unit) = self.units[id(o)]
        if (weak() == None):
            raise GarbageError
        return unit

# default unit map
unit_map = UnitMap()

def map_to_unit(unit: object, map: UnitMap = unit_map): # -> ((o: object) -> object) requires Python 3.11
    """Decorate functions or classes with units."""
    def wrap(o: object) -> object:
        map.map_to_unit(o, unit)
        return o
    return wrap

def get_unit_of(o: object) -> object:
    """Get unit from default map."""
    return unit_map.get_unit_of(o)
