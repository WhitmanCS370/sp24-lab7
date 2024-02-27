class Raises:
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_type != self.expected_exception:
            raise exception_type(exception_value)


def function_to_test(n):
    result = n / 0
    return result

# with Raises(ZeroDivisionError):
#     function_to_test(8)

import time

class Timer:

    def __init__(self):
        self.start_time = None

    def elapsed(self):
        return time.time() - self.start_time

    def __enter__(self):
        
        self.start_time = time.time()
        
        return self

    def __exit__(self, *args):
        # self.end_time = time.time()
        pass

with Timer() as start:
    print(start.elapsed())

