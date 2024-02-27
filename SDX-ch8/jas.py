# testing exceptions attempt.
class Jas():
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            assert exc_type == exc_value, "No Exception Raised"


# timer.
import time

class Timer:
    def __init__(self) -> None:
        # define start time.
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.perf_counter()
    
    def stop(self):
        return self.start_time
    
    def __enter__(self):
        # as we enter, lets start our timer.
        self.start()
        self.start_time = time.time()
        
    def __exit__(self):
        self.stop()
        #self.start_time = time.time() - self.start_time

with Timer() as start:
    time.sleep(3)
    