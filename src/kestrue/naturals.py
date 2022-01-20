from functools import reduce

zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))
four = lambda f: lambda x: f(f(f(f(x))))
five = lambda f: lambda x: f(f(f(f(f(x)))))


def succ(nat):
    return lambda f: lambda x: f(nat(f)(x))


def to_int(nat):
    return nat(lambda acc: acc + 1)(0)


def from_int(i):
    return reduce(lambda acc, _: succ(acc), range(i), zero)
