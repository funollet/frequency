#!/usr/bin/env python
# freq.py
# https://xkcd.com/1331/

from apscheduler.scheduler import Scheduler
from datetime import datetime, timedelta
import atexit


SECONDS_UP = 0.5
DEBUG = True

sched = Scheduler(daemon=True)

def log(msg):
    if DEBUG:
        print '%s: %s' % (datetime.now(), msg)


def ding():
    log("ding")
    sched.add_date_job(dong, datetime.now() + timedelta(0, SECONDS_UP, 0))

def dong():
    log("dong")


def tilin():
    log("   tilin")
    sched.add_date_job(tolon, datetime.now() + timedelta(0, SECONDS_UP, 0))

def tolon():
    log("   tolon")


def main():

    atexit.register(lambda: sched.shutdown(wait=False))

    sched.add_interval_job(ding, seconds=1)
    sched.add_interval_job(tilin, seconds=3)
    sched.start()
    while True:
        pass


if __name__ == '__main__':
    main()

