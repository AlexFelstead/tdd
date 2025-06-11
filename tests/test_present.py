import pytest
from lib.present import *

def test_input_is_None():
    present = Present()
    assert present.contents == None

def test_wrap_exception_error():
    present = Present()
    present.wrap("ugly woolen socks")

    with pytest.raises(Exception) as e:
        present.wrap("ugly woolen scarf")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap_exception_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_unwrapping():
    present = Present()
    present_to_wrap = "ugly woolden hat"
    present.wrap(present_to_wrap)
    present_to_unwrap = present.unwrap()
    assert present_to_wrap == present_to_unwrap