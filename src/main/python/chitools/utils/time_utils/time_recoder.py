import time
import functools

import pandas as pd

import logging
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

    def end(self):
        self._time_interval.append(["end", time.perf_counter_ns()])
        return (self._time_interval[-1][1]-self._time_interval[0][1])/1e9
    
    def get_cost_time(self):
        res = list()
        for pre, cur in zip(self._time_interval[:-1], self._time_interval[1:]):
            section_name = cur[0]
            used_time = (cur[1] - pre[1]) / 1e9
            res.append([section_name, used_time])
        return res
    
    def log_time(self):
        _log_record = "Time Record:"
        for section_name, used_time in self.get_cost_time():
            _log_record += f'\n{section_name:>12s} Used {used_time:>9.3f} Second'
        logger.info(_log_record)

    def get_record(self):
        return pd.DataFrame(self.get_cost_time())

def time_recorder(func):
    @functools.wraps(func)
    def wraper(*args, **kwargs):
        _timer = TimeRecoder()
        res = func(*args, **kwargs)
        _timer.add_interval(func.__name__)
        return res
    return wraper