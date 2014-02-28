#!/usr/bin/env python
# freq.py
# https://xkcd.com/1331/

import time
import threading



ACTIVE_TIME=0.5     # default time between on() and off() (in seconds)


class OnOff():
    """Cycles running two provided functions with a configurable period.
    Works in its own thread, so the main program is isolated from sleep()
    or blocking operations.
    """

    def __init__(self, period, on, off, active_time=ACTIVE_TIME):
        """Initialize class attributes.

        Arguments:
            period:      duration of service in 'off' status (seconds)
            on:          funtion called to activate service
            off:         funtion called to deactivate service
            active_time: (optional) duration of service in 'on' status (seconds)
        """
        self.period = period
        self.on = on
        self.off = off
        self.active_time = active_time


    def wait(self):
        """Call run() after 'period' in a new thread.
        """
        threading.Timer(self.period, self.run).start()


    def run(self):
        """Run on(), sleep, run off(), call run().

        wait() and run() create an endless loop in its own thread.
        """
        self.on()
        time.sleep(self.active_time)
        self.off()
        self.wait()


############################################################

def ding():
    print "ding"

def dong():
    print "dong"

def tilin():
    print "   tilin"

def tolon():
    print "   tolon"


def main():
    # Print 'ding' and 'dong' every second.
    OnOff(1, ding, dong).wait()
    # Print 'tilin' and 'tolon' every 3 seconds.
    OnOff(3, tilin, tolon).wait()



if __name__ == '__main__':
    main()

