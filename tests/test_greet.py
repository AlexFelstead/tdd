from lib.greet import *

def test_greet():
    result = greet("Alex")
    assert result == "Hello, Alex!"