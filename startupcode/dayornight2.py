from datetime import datetime, time
import subprocess

def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end


if in_between(datetime.now().time(), time(21), time(6)):
    print "Night"
    subprocess.call('sudo python plug1switchoff.py', shell=True)
else:
    print "Day"
    subprocess.call('sudo python plug1switchon.py', shell=True)

#print("night" if in_between(datetime.now().time(), time(21), time(6)) else "day")
