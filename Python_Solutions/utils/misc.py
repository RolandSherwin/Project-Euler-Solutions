import time
import re


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        elapsed = (te-ts)
        print(f"{method.__name__} took: {elapsed} ms")
        return result
    return timed


def preprocess_data(number_as_string):
    # Removes special characters and put them in list. You have to process after
    # this
    arr = re.findall(r"[\w']+", number_as_string)
    return arr
