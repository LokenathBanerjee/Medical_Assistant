import time

class SimpleRateLimiter:
    def __init__(self, min_interval_sec: float = 1.0):
        self.min_interval_sec = min_interval_sec
        self._last = 0.0

    def wait(self):
        now = time.time()
        gap = now - self._last
        if gap < self.min_interval_sec:
            time.sleep(self.min_interval_sec - gap)
        self._last = time.time()

