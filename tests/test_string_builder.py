from lib.string_builder import *

def test_input_is_string():
    builder = StringBuilder()
    assert builder.str == ""

def test_add_one_string():
    builder = StringBuilder()
    builder.add("one")
    assert builder.str

def test_add_two_strings():
    builder = StringBuilder()
    builder.add("two")
    builder.add("three")
    assert builder.str

def test_string_length():
    builder = StringBuilder()
    builder.add("four")
    assert builder.size() == 4

def test_string_length_with_multiple_strings():
    builder = StringBuilder()
    builder.add("four")
    builder.add("eight")
    assert builder.size() == 9

def test_output():
    builder = StringBuilder()
    builder.add("duck")
    assert builder.output() == "duck"