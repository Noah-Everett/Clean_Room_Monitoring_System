# use file instead of sensorCode.py to run code on a system without sensors

import random
import time

def getReading( key ): # returns random numbers for each sensor reading
    time.sleep( .005 ) # slows down code
    if key == "Temperature_MS8607": return random.random()
    elif key == "Humidity_MS8607": return random.random()
    elif key == "Pressure": return random.random()
    elif key == "Temperature_DHT22": return random.random()
    elif key == "Humidity_DHT22": return random.random()
    elif key == "Dust_PM10Standard": return random.random()
    elif key == "Dust_PM25Standard": return random.random()
    elif key == "Dust_PM100Standard": return random.random()
    elif key == "Dust_PM10Env": return random.random()
    elif key == "Dust_PM25Env": return random.random()
    elif key == "Dust_PM100Env": return random.random()
    elif key == "Dust_Particles03um": return random.random()
    elif key == "Dust_Particles05um": return random.random()
    elif key == "Dust_Particles10um": return random.random()
    elif key == "Dust_Particles25um": return random.random()
    elif key == "Dust_Particles50um": return random.random()
    elif key == "Dust_Particles100": return random.random()
    elif key == "VolatileOrganicCompounds_eCO2": return random.random()
    elif key == "VolatileOrganicCompounds_TVOC": return random.random()