from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    start = time.perf_counter()
    yield
    print(f"{name}: {time.perf_counter() - start:.2f}s")