import time
import logging
import functools

import pandas as pd

logger = logging.getLogger(__name__)
class SingletonClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._initialized = False
        return cls._instance

    def clear(cls):
        delattr(cls.__class__, "_instance")
        delattr(cls.__class__, "_initialized")
class TimeRecoder(SingletonClass):
    def __init__(self):
        if self._initialized: return
        self._initialized = True
        self._started = True
        self._time_interval: list[tuple[str, int]] = list()
        self._time_interval.append(["start", time.perf_counter_ns()])

    def add_interval(self, label: str=None):
        label = f'Section {len(self._time_interval)}' if label is None else label
        self._time_interval.append([label, time.perf_counter_ns()])

    def get_total_exec_time(self) -> float:
        return (self._time_interval[-1][1]-self._time_interval[0][1])/1e9

    def get_exec_time(self) -> list[tuple[str, float]]:
        return [(cur[0], (cur[1]-pre[1])/1e9) for pre, cur in zip(self._time_interval[:-1], self._time_interval[1:])]

    def log_exec_time(self):
        _log_record = "Time Record:"
        for section_name, used_time in self.get_exec_time():
            _log_record += f'\n{section_name:>25s}\tUsed {used_time:>9.3f} sec'
        logger.info(_log_record)

    def record_exec_time(self):
        self.log_exec_time()
        return pd.DataFrame(self.get_exec_time(), columns=["Section", "Execution Time"])

def time_recorder(func):
    @functools.wraps(func)
    def wraper(*args, **kwargs):
        _timer = TimeRecoder()
        res = func(*args, **kwargs)
        _timer.add_interval(func.__name__)
        return res
    return wraper