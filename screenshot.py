#! /usr/bin/env python

import sys
import os
import time

from com.dtmilano.android.viewclient import ViewClient
# start_time = time.time()
def screenshot(name):
    filename = name or str(time.time()) + '.png'
    device, serialno = ViewClient.connectToDeviceOrExit(verbose=False)
    device.takeSnapshot().save(filename, 'PNG')

    # print("--- %s seconds ---" % (time.time() - start_time))

# screenshot('inRoom.png')