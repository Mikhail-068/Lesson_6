from main import ex
import math


def test_filter(ex=ex):
    assert list(filter(lambda x: len(x) < 5, ex)) == ['лиса']


def test_map(ex=ex):
    assert list(map(len, ex)) == [4, 7, 6]


def test_sorted(ex=ex):
    assert sorted(ex, key=lambda x: x[-1]) == ['лиса', 'собака', 'медведь']


def test_pi():
    assert math.pi == 3.141592653589793


def test_sqrt():
    assert math.sqrt(4) == 2.0


def test_pow():
    assert math.pow(4,2) == 16.0


def test_hypot():
    assert math.hypot(4,1) == 4.123105625617661