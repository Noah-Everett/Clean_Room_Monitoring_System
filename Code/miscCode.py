import math

def pad( num, nDigits ): # returns num with 0 padding so it has nDigits
    if num == 0: 
        return "0"
    
    padding = ""
    size = math.pow( 10, nDigits - 1 )
    
    if num < size:
        while int( num / size ) < 1:
            padding += "0"
            num *= 10
    
    return padding

def printTime( totalSeconds ): # returns time in nicely formatted string
    seconds = math.floor( totalSeconds ) % 60
    minutes = math.floor( totalSeconds / 60 ) % 60
    hours = math.floor( totalSeconds / 3600 ) % 24
    days = math.floor( totalSeconds / 86400 )
    
    return str( days ) + " Days " + pad( hours, 2 ) + str( hours ) + ":" + pad( minutes, 2 ) + str( minutes ) + ":" + pad( seconds, 2 ) + str( seconds )