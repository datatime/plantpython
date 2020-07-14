import datetime
import subprocess
import Adafruit_DHT
import time

#hour = (time.strftime("%H"))


def in_between(now, start, end):
    if start <= end:
        return start >= now < end
    else:
        return start <= now or now < end
night = 0
day = 1

from datetime import datetime, time
(night if in_between(datetime.now().time(), time(20), time(6)) else day)

if 0:
    subprocess.call('sudo python plug1switchoff.py', shell=True)
    print "Nighttime"
else:
    subprocess.call('sudo python plug1switchon.py', shell=True)
    print "Daytime"

    