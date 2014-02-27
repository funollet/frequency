#!/usr/bin/env python
# freq.py
# https://xkcd.com/1331/

import time
import threading


class Ding():

    def wait(self):
        threading.Timer(1, self.run).start()

    def run(self):
        print "ding"
        time.sleep(0.2)
        print "dong"
        self.wait()


class Tilin():

    def wait(self):
        threading.Timer(3, self.run).start()

    def run(self):
        print "   tilin"
        time.sleep(0.5)
        print "   tolon"
        self.wait()



def main():
    Tilin().wait()
    Ding().wait()



if __name__ == '__main__':
    main()

