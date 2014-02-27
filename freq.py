#!/usr/bin/env python
# freq.py
# https://xkcd.com/1331/

import time
import threading

class Freq:
    """Execute a function if elapsed time > period.
    """

    def __init__(self, period):
        self.origin = time.time()
        self.period = period


    def regular(self):
        lapse = time.time() - self.origin
        if lapse > self.period:
            self.origin = time.time()
            self.callback()


    def callback(self):
        pass


class Ding(Freq):
    def callback(self):
        print 'ding'

class Dong(Freq):
    def callback(self):
        print 'DONG!!!!'



def main():
    every_second = Ding(1)
    every_three = Dong(3)

    while(True):
        time.sleep(0.05)
        every_second.regular()
        every_three.regular()



if __name__ == '__main__':
    main()

