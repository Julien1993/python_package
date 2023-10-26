
# Imports
import timeit
import numpy as np

# Constants
MEAN_REPETITIONS = 10

# Decorators
def timer(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        print(f"Time elapsed in {func.__name__} took : {end - start} seconds")
        return result
    return wrapper

def mean_timer(n=MEAN_REPETITIONS):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time = timeit.repeat(lambda: func(*args, **kwargs), number=n, repeat=1)
            result = func(*args, **kwargs)
            print(f"Mean time elapsed in {func.__name__} took : {np.mean(time)} seconds")
            return result
        return wrapper
    return decorator
