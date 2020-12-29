import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        elapsed = (te-ts)
        print(f"{method.__name__} took: {elapsed} ms")
        return result
    return timed
