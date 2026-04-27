import pytest
from app import add

def test_add_positive():
    list1 = [1, 2, 3, 4, 5, 6]
    assert add(list1) == 209

def test_add_negative():
    list2 = [-1, -2, -3, -4, -5, -6]
    assert add(list2) == -97

def test_add_float():
    list3 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
    assert add(list3) == 586.971

def test_add_invalid():
    with pytest.raises(ValueError):
        add("2", 3)
