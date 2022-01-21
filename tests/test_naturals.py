import pytest

from kestrue import naturals as N

ti = N.to_int
fi = N.from_int

def test_naturals():
    assert ti(N.one) == 1
    assert ti(N.two) == 2
    assert ti(N.three) == 3
    assert ti(N.four) == 4
    assert ti(N.five) == 5


@pytest.mark.parametrize("i", range(100))
def test_int(i):
    assert ti(fi(i)) == i


def test_successor():
    curr = N.zero
    for _ in range(100):
        nxt = N.succ(curr)
        assert ti(curr) + 1 == ti(nxt)
        curr = nxt


@pytest.mark.parametrize(["a", "b", "c"], [
    (0, 0, 0),
    (0, 1, 1),
    (2, 8, 10),
    (100, 150, 250),
])
def test_addition(a: int, b: int, c: int):
    assert ti(N.add(fi(a))(fi(b))) == ti(N.add(fi(a))(fi(b))) == c
