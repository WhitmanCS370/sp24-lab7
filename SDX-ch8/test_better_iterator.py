import pytest
from better_iterator import BetterIterator

def gather(buffer):
    result = ""
    for char in buffer:
        result += char
    return result

def test_naive_buffer():
    buffer = BetterIterator(["ab", "c"])
    assert gather(buffer) == "abc"

# [example]
def test_naive_buffer_nested_loop():
    buffer = BetterIterator(["a", "b"])
    result = ""
    for _ in buffer:
        for inner in buffer:
            result += inner
    assert result == "abab"
    
def test_naive_empty():
    buffer = BetterIterator(["a", ""])
    assert gather(buffer) == "a"
# [/example]

if __name__ == "__main__":
    test_naive_buffer()
    test_naive_buffer_nested_loop()
    test_naive_empty()