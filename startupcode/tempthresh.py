import datetime
import subprocess
import Adafruit_DHT
import time

Humidity, Temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 5)
Temperature = int(Temperature)
Humidity = int(Humidity)

if Temperature < 17:
    subprocess.call('sudo python plug2switchon.py', shell=True)
    "Too cold switching on heatpad"
else:
    subprocess.call('sudo python plug2switchoff.py', shell=True)