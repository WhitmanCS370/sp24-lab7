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