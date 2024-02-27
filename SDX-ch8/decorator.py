def wrap(log):
    def _decorator(func):
        with open.file('log.txt', 'a') as f:
            f.write('Function {} was called\n'.format(func.__name__))
        def _inner(*args):
            # some function
            return func(*args)