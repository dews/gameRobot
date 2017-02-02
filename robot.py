#! /usr/bin/env python
import sys
import time
import re
import os
import subprocess
import matchImage
import screenshot

try:
    sys.path.insert(0, os.path.join(
        os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

from com.dtmilano.android.adb.adbclient import AdbClient
from com.dtmilano.android.common import obtainAdbPath


class main():

    def __init__(self):
        self.round = 1
        try:
            adbClient = AdbClient('fakeserialno', settransport=False)
        except RuntimeError, ex:
            if re.search('Connection refused', str(ex)):
                raise RuntimeError("adb is not running")
            raise(ex)
        devices = adbClient.getDevices()

        if len(devices) == 0:
            raise RuntimeError(
                "This tests require at least one device connected. None was found.")
        for device in devices:
            if device.status == 'device':
                sn = device.serialno
                self.adbClient = AdbClient(sn)

                print('Robot start')
                while True:
                    print('Round: %s', self.round)
                    self.round = self.round + 1
                    self.retry = 0
                    time.sleep(2)
                    self.adbClient.touch(2385, 1158)
                    time.sleep(2)
                    self.adbClient.touch(1930, 1070)
                    time.sleep(3)
                    self.inRoom()
                    print('End room')

    def inRoom(self):
        screenshot.screenshot('inRoom.png')
        (w, h) = matchImage.matchImage('inRoom.png', 'boss.png')

        if w != False:
            print('Find Boss')
            self.adbClient.touch(w, h)
            # Fight
            time.sleep(120)
            # Finish fight
            self.adbClient.touch(1300, 640)
            # Take itmes
            time.sleep(3)
            self.adbClient.touch(1300, 640)
            # Animantion
            time.sleep(8)
            self.findBox()
        else:
            (w, h) = matchImage.matchImage('inRoom.png', 'demon.png')

            if w != False:
                print("Find demon")
                self.gotoBattle(w, h)

            else:
                print("Can't find demon", self.retry)
                # Move to other place
                if self.retry < 6:
                    self.adbClient.touch(2200, 1100)
                else:
                    self.adbClient.touch(400, 1100)
                    if self.retry > 12:
                        self.retry = 0
                self.retry = self.retry + 1
                time.sleep(2)

            if not self.isInMap():
                print('Not in map')
                self.inRoom()

    def gotoBattle(self, w, h):
        self.adbClient.touch(w - 200, h)
        self.adbClient.touch(w - 100, h)
        self.adbClient.touch(w, h)
        self.adbClient.touch(w + 100, h)
        self.adbClient.touch(w + 200, h)

        time.sleep(3)
        screenshot.screenshot('inRoom.png')
        (w, h) = matchImage.matchImage('inRoom.png', 'isInRoom.png')

        if w:
            print('Not in battle', w, h)
        else:
            # Fight
            time.sleep(50)
            # Finish fight
            self.adbClient.touch(1300, 840)
            # Take itmes
            time.sleep(3)
            self.adbClient.touch(1300, 840)
            # Animantion
            time.sleep(4)

    def isInMap(self):
        screenshot.screenshot('inRoom.png')
        (w, h) = matchImage.matchImage('inRoom.png', 'isInMap.png', 250000000)
        print 'map'
        if w:
            return True
        else:
            return False

    def findBox(self):
        screenshot.screenshot('inRoom.png')
        (w, h) = matchImage.matchImage('inRoom.png', 'box.png')

        if w != False:
            print("Find box")
            self.adbClient.touch(w, h)
            time.sleep(2)
            self.adbClient.touch(2200, 730)
            time.sleep(2)
            self.findBox()
        else:
            print("Can't find box")
            return False

if __name__ == "__main__":
    main()
