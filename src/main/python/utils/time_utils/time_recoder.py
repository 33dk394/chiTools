import time

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
    def __init__(self, start: bool=False):
        if self._initialized: return
        self._initialized = True
        self.__started = False
        self.__time_interval: list[tuple[str, int]] = list()

        if start:
            self.__started = True
            self.__time_interval.append(["start", time.perf_counter_ns()])

    def start(self):
        if not self.__started:
            self.__started = True
            self.__time_interval.append(["start", time.perf_counter_ns()])

    def add_interval(self, label: str=None):
        if self.__started:
            label = f'Section {len(self.__time_interval)}' if label is None else label
            self.__time_interval.append([label, time.perf_counter_ns()])

    def end(self):
        if self.__started:
            self.__time_interval.append(["end", time.perf_counter_ns()])
            return (self.__time_interval[-1][1]-self.__time_interval[0][1])/1e9
    
    def evaluate(self):
        for pre, cur in zip(self.__time_interval[:-1], self.__time_interval[1:]):
            section_name = cur[0]
            used_time = (cur[1] - pre[1]) / 1e9
            print(f'{section_name:>12s} Used {used_time:>9.3f} Second')
