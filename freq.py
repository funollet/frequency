#!/usr/bin/env python
# freq.py
# https://xkcd.com/1331/

from apscheduler.scheduler import Scheduler
from datetime import datetime, timedelta
import atexit


SECONDS_UP = 0.5
DEBUG = True


def log(msg):
    if DEBUG:
        print '%s: %s' % (datetime.now(), msg)


class Pwm(object):

    def __init__(self, pin, period, duration):
        self.pin = pin
        self.period = period
        self.duration = duration
        # Call on() in a new thread.
        sched.add_interval_job(self.__on, seconds=self.period)

    def __on(self):
        log('%s On' % self.pin)
        off_time = datetime.now() + timedelta(0, self.duration, 0)
        # Schedule off() to run, in another thread, after 'off_time'.
        sched.add_date_job(self.__off, off_time)

    def __off(self):
        log('%s Off' % self.pin)


def main():
    Pwm("ding  ", 1, SECONDS_UP)
    Pwm("  DONG", 3, SECONDS_UP)
    sched.start()
    while True:
        pass


if __name__ == '__main__':
    sched = Scheduler(daemon=True)
    atexit.register(lambda: sched.shutdown(wait=False))

    main()

