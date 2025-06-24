from lib.report_length import *

def test_report_length():
    assert report_length("A look into space") == "This string was 17 characters long."
    assert report_length("A bee stung me :(") == "This string was 17 characters long."
    assert report_length("no") == "This string was 2 characters long."
    assert report_length("yes") == "This string was 3 characters long."