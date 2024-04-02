import time


class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        print(time.time() - self.start)


with Timer():
    time.sleep(5)
