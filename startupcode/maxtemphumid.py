import datetime
import subprocess
import Adafruit_DHT
import time

Humidity, Temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 5)
Temperature = int(Temperature)
Humidity = int(Humidity)

if (Temperature > 24) or (Humidity > 80):
    subprocess.call('sudo python evacuateair.py', shell=True)
    print "Too warm or humid, activating fans"