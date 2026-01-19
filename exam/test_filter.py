
from main import filter_positive

def test_mixed_list():
    assert filter_positive([1, -2, 3, -4, 5]) == [1, 3, 5]

def test_only_negative():
    assert filter_positive([-1, -5, -10]) == []

def test_empty_list():
    assert filter_positive([]) == []
