import board
import busio

import adafruit_dht as DHT22
from adafruit_ms8607 import MS8607
from adafruit_pm25.i2c import PM25_I2C as PMSA003I
import adafruit_sgp30 as SGP30

i2c = busio.I2C( board.SCL, board.SDA )

dht22 = DHT22.DHT22( board.D4 )
ms8607 = MS8607( i2c )
pmsa003i = PMSA003I( i2c, None )
sgp30 = SGP30.Adafruit_SGP30( i2c )

def getReading( key ): # get and return reading
    if key == "Temperature_MS8607": 
        valid = False

        while not valid:
            try:
                return ms8607.temperature
            except RuntimeError:
                valid = False
                
    elif key == "Humidity_MS8607": 
        valid = False

        while not valid:
            try:
                return ms8607.relative_humidity
            except RuntimeError:
                valid = False

    elif key == "Pressure": 
        valid = False

        while not valid:
            try:
                return ms8607.pressure * 0.750016827
            except RuntimeError:
                valid = False

    elif key == "Temperature_DHT22": 
        valid = False

        while not valid:
            try:
                return dht22.temperature
            except RuntimeError:
                valid = False

    elif key == "Humidity_DHT22": 
        valid = False

        while not valid:
            try:
                return dht22.humidity
            except RuntimeError:
                valid = False

    elif key == "Dust_PM10Standard": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "pm10 standard" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_PM25Standard": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "pm25 standard" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_PM100Standard": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "pm100 standard" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_PM10Env": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "pm10 env" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_PM25Env": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "pm25 env" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_PM100Env": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "pm100 env" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_Particles03um": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "particles 03um" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_Particles05um": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "particles 05um" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_Particles10um": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "particles 10um" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_Particles25um": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "particles 25um" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_Particles50um": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "particles 50um" ] * 10
            except RuntimeError:
                valid = False

    elif key == "Dust_Particles100": 
        valid = False

        while not valid:
            try:
                return pmsa003i.read()[ "particles 100um" ] * 10
            except RuntimeError:
                valid = False

    elif key == "VolatileOrganicCompounds_eCO2": 
        valid = False

        while not valid:
            try:
                return sgp30.iaq_measure()[ 0 ]
            except RuntimeError:
                valid = False

    elif key == "VolatileOrganicCompounds_TVOC": 
        valid = False

        while not valid:
            try:
                return sgp30.iaq_measure()[ 1 ]
            except RuntimeError:
                valid = False