import datetime
import subprocess
import Adafruit_DHT
import time

while True:
    
    #Humidity, Temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 5)
    #Temperature = int(Temperature)
    #Humidity = int(Humidity)
    
    print "----------Beginning 30 second mark check----------"
    
    #print Temperature, "c"
    #print Humidity, "%"
    
    #LIGHTS, PLUG 1
    subprocess.call('sudo python dayornight2.py', shell=True)
    
    #WATER PLANT
    subprocess.call('sudo python waterplant.py', shell=True)   
    
    #HEATPAD, PLUG 2
    subprocess.call('sudo python tempthresh.py', shell=True)
        
    #EVACUATE ALL AIR
    subprocess.call('sudo python maxtemphumid.py', shell=True)

    time.sleep(30)   
