import Adafruit_DHT
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.output(12, 1)
GPIO.output(16, 1)
GPIO.output(20, 1)
time.sleep(5)
GPIO.output(12, 0)
GPIO.output(16, 0)
GPIO.output(20, 0)
GPIO.cleanup()

