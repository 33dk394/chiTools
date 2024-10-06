import time

import logging
logger = logging.getLogger(__name__)
from chitools.utils.time_utils.time_recoder import TimeRecoder, time_recorder

@time_recorder
def app1():
    time.sleep(0.5)

@time_recorder
def app2():
    time.sleep(0.5)

@time_recorder
def app3():
    time.sleep(0.5)

def main():
    app1()
    app2()
    app3()
    print("Chi Tools Done")
    TimeRecoder().record_exec_time().to_csv("./Test.csv", index=False)


if __name__ == "__main__":
    main()