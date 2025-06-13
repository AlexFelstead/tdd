
# Pair Challenge Number 3


from lib.high_value import *

def test_get_highest_first():
    hv = HighValue(10, 5)
    assert hv.get_highest() == "First value is higher"

def test_get_highest_second_value():
    hv = HighValue(515, 1620)
    assert hv.get_highest() == "Second value is higher"

def test_both_are_equal():
    hv = HighValue(1010, 1010)
    assert hv.get_highest() == "Values are equal"

def test_first_in_add_function():
    hv = HighValue(20, 25)
    hv.add(5, "first")
    assert hv.value_first == 25

def test_second_in_add_function():
    hv = HighValue(20, 25)
    hv.add(5, "second")
    assert hv.value_second == 30











