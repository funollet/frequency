#!/usr/bin/env python
# freq.py
# https://xkcd.com/1331/

import time
import threading


def ding_wait():
    threading.Timer(1, ding).start()

def ding():
    print "ding"
    time.sleep(0.2)
    print "dong"
    ding_wait()



def tilin_wait():
    t = threading.Timer(3, tilin).start()

def tilin():
    print "   tilin"
    time.sleep(0.5)
    print "   tolon"
    tilin_wait()






def main():
    ding_wait()
    tilin_wait()


if __name__ == '__main__':
    main()

