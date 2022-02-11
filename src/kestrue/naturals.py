from functools import reduce

zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))
four = lambda f: lambda x: f(f(f(f(x))))
five = lambda f: lambda x: f(f(f(f(f(x)))))


r"""
succ := \n.\fx.f(nfx)
>>> succ(2)
n -> \gy.g(gy)
-> fx.f(f(f(x))) # 3
"""
succ = lambda nat: lambda f: lambda x: f(nat(f)(x))


def to_int(nat):
    """
    >>> to_int(lambda f: lambda x: x)
    0
    >>> to_int(lambda f: lambda x: f(x))
    1
    >>> to_int(lambda f: lambda x: f(f(f(f(f(f(f(x))))))))
    7
    """
    return nat(lambda acc: acc + 1)(0)


def from_int(i):
    return reduce(lambda acc, _: succ(acc), range(i), zero)


r"""
add := \ab.\fx.af(bfx)
>>> add(2)(3)
a -> \gy.g(gy)
b -> \hz.h(h(hz))
-> \fx: f(f(bfx))
-> \fx: f(f(f(f(f(x))))) # 5
"""
add = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
