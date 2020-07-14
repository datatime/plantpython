import time
import RPi.GPIO as GPIO

fan2 = 16 # fan to draw air into the root chamber for moisture, nutrients or cooler air
fan3 = 20 # fan to draw air into the vaporising chamber to equalise the pressure for drawing in air to the root chamber

run = 2 # runtime to circulate air

#loopsleep = time.sleep(10) # sleep time between temp/humid loops

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan2,GPIO.OUT)
GPIO.setup(fan3,GPIO.OUT)

GPIO.output(fan2, 1)
GPIO.output(fan3, 1)
time.sleep(run)
GPIO.output(fan2, 0)
GPIO.output(fan3, 0)
GPIO.cleanup()