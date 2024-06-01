from unitsofmeasure import decprefix

def test():
    items = decprefix.prefixes.items()
    assert len(items) == 24 # there are 24 decimal prefixes

    for (key, prefix) in items:
        print(key, prefix)
        assert key == prefix.symbol
        assert prefix.base == 10
        assert prefix.exponent >= -30
        assert prefix.exponent <= 30
        assert len(prefix.symbol) > 0
        assert len(prefix.name) > 0

def test_order():
    prefixes = [
        decprefix.q,
        decprefix.r,
        decprefix.y,
        decprefix.z,
        decprefix.a,
        decprefix.f,
        decprefix.p,
        decprefix.n,
        decprefix.µ,
        decprefix.m,
        decprefix.c,
        decprefix.d,
        decprefix.da,
        decprefix.h,
        decprefix.k,
        decprefix.M,
        decprefix.G,
        decprefix.T,
        decprefix.P,
        decprefix.E,
        decprefix.Z,
        decprefix.Y,
        decprefix.R,
        decprefix.Q
    ]
    
    prev = None
    for prefix in prefixes:
        if prev is not None:
            print(prev, "<", prefix)
            assert prev < prefix
            assert prefix > prev
        prev = prefix
