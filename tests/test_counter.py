from lib.counter import *

def test_counter_adds():
    counter = Counter()
    result = counter.add(10)
    assert "Counted to 10 so far."
    
def test_counter_starts_at_0():
    counter = Counter()
    assert counter.count == 0

def test_counter_counts_multiple():
    counter = Counter()
    result = counter.add(10)
    result = counter.add(5)
    assert "Counted to 15 so far."

def test_no_input():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."