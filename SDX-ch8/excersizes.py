# Create a context manager called Timer that reports how long it has been since a block of code started running

""""
from time import time

class Timer:
    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, *args):
        from time import time
        print(time() - self.start)


with Timer() as start:
    # do something that takes time
    for i in range(100000000):
        pass
"""


# Modify the iterator example so that it handles empty strings correctly, i.e., so that iterating over the list ["a", ""] produces ["a"].

# [buffer]
class NaiveIterator:
    def __init__(self, text):
        self._text = text[:]

    def __iter__(self):
        self._row, self._col = 0, -1
        return self

    def __next__(self):
        self._advance()
        if self._row == len(self._text):
            raise StopIteration
        return self._text[self._row][self._col]
    
    def _advance(self):
        if self._row < len(self._text):
            self._col += 1
            if self._col == len(self._text[self._row]):
                self._row += 1
                self._col = 0


def gather(buffer):
    result = ""
    for char in buffer:
        result += char
    return result


def test_naive_buffer():
    buffer = NaiveIterator(["ab", "c"])
    if gather(buffer) == "abc":
        print("Passed")
        
        
if __name__ == "__main__":
    test_naive_buffer()