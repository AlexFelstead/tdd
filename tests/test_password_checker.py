import pytest
from lib.password_checker import *

def test_input():
    pw_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        pw_checker.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_length_under_eight():
    pw_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        pw_checker.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_length_equals_eight():
    pw_checker = PasswordChecker()
    password = pw_checker.check("12345678")
    assert password == True

def test_length_over_eight():
    pw_checker = PasswordChecker()
    password = pw_checker.check("123456789")
    assert password == True





# def test_input():
#     pw_checker = PasswordChecker()
#     with pytest.raises(Exception) as e:
#         pw_checker.check(None)

#     error_message = str(e.value)
#     assert error_message == "Invalid password, must be 8+ characters."