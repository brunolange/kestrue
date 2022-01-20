from kestrue import combinators as c

def test_identity():
    assert c.I(1) == 1
    assert c.I("test") == "test"
    assert c.I(None) is None

def test_kestrel():
    assert c.K(1)(2) == 1
    assert c.K(None)(2) is None

def test_kite():
    assert c.KI(1)(2) == 2
    assert c.KI(None)(2) == 2
    assert c.KI(1)(None) is None

def test_cardinal():
    assert c.CA(lambda a: lambda b: a - b)(2)(10) == 8
    assert c.CA(lambda a: lambda b: a + b)("bar")("foo") == "foobar"
    