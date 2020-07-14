import time
import subprocess
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

time.sleep(1)
#(time.strftime("%H:%M:%S"))
minute = (time.strftime("%M"))
m = int((time.strftime("%M"))[1])

if (m == 0) or (m == 5):
    print "Watering time"
    #vape
    subprocess.call('sudo python plug4switchon.py', shell=True)
    time.sleep(3)
    subprocess.call('sudo python plug4switchoff.py', shell=True)
    #fan
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20, 1)
    time.sleep(5)
    GPIO.output(20, 0)
    GPIO.cleanup

else:
    print "Not watering time"
