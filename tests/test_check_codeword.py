from lib.check_codeword import *

def test_check_codeword():
    assert check_codeword("horse") == "Correct! Come in."
    assert check_codeword("hose") == "Close, but nope."
    assert check_codeword("banana") == "WRONG!"