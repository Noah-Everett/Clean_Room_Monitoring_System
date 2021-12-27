import pandas as pd
import os

import config

def getData( fileDir ): # gets data for plotting
    valid = False
    while not valid:
        try: 
            data = pd.read_csv( fileDir )
            if data[ "Run Time" ].iloc[ -1 ] - data[ "Run Time" ][ 0 ] >= config.plotRange - 2: # check for correct length
                return data
            else: 
                continue
        except: 
            continue

def getRunName(): # returns name of lastest run that is being plotted
    os.chdir( config.dataDir )
    
    runs = []
    for file in sorted( os.listdir( os.getcwd() ) ):
        if file != ".DS_Store": runs.append( file )
        
    return runs[ -1 ]