from lib.gratitudes import *

def test_list_is_empty():
    x = Gratitudes()
    assert x.gratitudes == []

def test_appending_list_once():
    x = Gratitudes()
    x.add("beans")
    assert x.gratitudes == ["beans"]

def test_appending_list_twice():
    x = Gratitudes()
    x.add("beans")
    x.add("on")
    
def test_appending_list_thrice():
    x = Gratitudes()
    x.add("beans")
    x.add("on")
    x.add("toast")
    assert x.gratitudes == ["beans", "on", "toast"]

def test_output():
    x = Gratitudes()
    x.add("beans")
    x.add("on")
    x.add("toast")
    assert x.format() == "Be grateful for: beans, on, toast"

def test_another_way_if_list_is_empty():
    x = Gratitudes()
    assert x.format() == "Be grateful for: "