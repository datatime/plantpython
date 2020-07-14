import Adafruit_DHT
import time
import RPi.GPIO as GPIO

Humidity, Temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 5)
Temperature = int(Temperature)
Humidity = int(Humidity)


GPIO.setmode(GPIO.BCM)
GPIO.setup( fan for cooler pin ... ,GPIO.OUT)
GPIO.output( fan for cooler pin ... , 1)
time.sleep(5)
GPIO.output( fan for cooler pin ... , 0)
GPIO.cleanup