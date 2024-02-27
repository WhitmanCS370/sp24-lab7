from mock_object import Fake
import pytest
from util import run_tests

def WrongExepctionError(Exception):
    pass

# [contextraises]
class Raises(Fake):
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type == None:
            raise AssertionError(f"{self.expected_exception.__name__} was not raised")
        if not issubclass(exc_type, self.expected_exception):
            raise AssertionError("Expected exception %s but got %s" % (self.expected_exception, exc_type))

        return True





# [contextfake]
class ContextFake(Fake):
    def __init__(self, name, func=None, value=None):
        super().__init__(func, value)
        self.name = name
        self.original = None

    def __enter__(self):
        assert self.name in globals()
        self.original = globals()[self.name]
        globals()[self.name] = self
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        globals()[self.name] = self.original
# [/contextfake]

# [test]
def subber(a, b):
    return a - b

def check_no_lasting_effects():
    assert subber(2, 3) == -1
    with ContextFake("subber", value=1234) as fake:
        assert subber(2, 3) == 1234
        assert len(fake.calls) == 1
    assert subber(2, 3) == -1
# [/test]

def test_raises():
    with Raises(ZeroDivisionError):
        1 / 0

    with Raises(ValueError):
        raise ValueError("foo")

    with pytest.raises(AssertionError):
        with Raises(ZeroDivisionError):
            pass

if __name__ == "__main__":
    run_tests(globals(), "check_")
