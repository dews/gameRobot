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
                self.room()

    def room(self):
        icon = [
            {"x": 765, "y": 330}, {"x": 1475, "y": 330}, {"x": 2125, "y": 330},
            {"x": 765, "y": 560}, {"x": 1475, "y": 560}, {"x": 2125, "y": 560},
            {"x": 765, "y": 790}, {"x": 1475, "y": 790}, {"x": 2125, "y": 790}
        ]

        for index, item in enumerate(icon):
            print(index, item)
            # if index == 0 or index == 1 or index == 3:
            #     pass
            # else:
            self.fight(item)

    def fight(self, location):
        self.adbClient.touch(location["x"], location["y"])
        time.sleep(1)
        self.adbClient.touch(location["x"], location["y"] + 180)
        time.sleep(7)
        self.adbClient.touch(2350, 1135)
        time.sleep(150)
        # Finish fight
        self.adbClient.touch(1300, 840)
        # Take itmes
        time.sleep(3)
        self.adbClient.touch(1300, 840)
        # Animantion
        time.sleep(4)
        # Every 3, 9, 12 wins, take gift
        self.adbClient.touch(316, 927)
        time.sleep(2)
        self.adbClient.touch(316, 927)
        time.sleep(2)

if __name__ == "__main__":
    main()
