import pandas as pd
import os
import time
import datetime as dt

import sensorCode
# import sensorCode_random as sensorCode # use if running without sensors
import miscCode
import config

def makeDataFiles(): # makes run folder and data files
    os.chdir( config.dataDir )

    # get run files
    runs = []
    for file in sorted( os.listdir( os.getcwd() ) ):
        if file != ".DS_Store": runs.append( file )

    # make new run file name   
    if len( runs ) == 0: 
        runNum = 1
    else: 
        runNum = int( runs[ -1 ][ len( "Run" ): ] ) + 1
    runPadding = miscCode.pad( runNum, 4 )
    runName = "Run" + runPadding + str( runNum )

    # make new run file
    os.makedirs( config.dataDir + "/" + runName )
    os.chdir( config.dataDir + "/" + runName )

    # make csv data files
    open( "Data0.csv", "a" ).close()
    open( "Data1.csv", "a" ).close()

    # print run start message
    print( "Starting run", runName )

    return runName

def initDataFrame(): # initiate pandas data frame
    return pd.DataFrame( columns = config.dataTypes )

def updateData( data, runTime_current ): # gets and returns data from all sensors
    # make dictionaly of all data
    newData = {}
    for key in data:
        if key == "Actual Time": 
            newData.update( { key: time.time() } )
        elif key == "Run Time": 
            newData.update( { key: runTime_current } )
        elif key == "Date Time": 
            newData.update( { key: dt.datetime.now() } )
        else: 
            newData.update( { key: sensorCode.getReading( key ) } )

    return data.append( newData, ignore_index = True )

def updateFile( data, file ): # adds data to file
    if file == "Data0.csv": 
        if len( data ) <= 3: # for beginning of run
            data.to_csv( str( os.getcwd() ) + "/Data0.csv", index = False ) 
        else: # for rest of run
            data.iloc[ -2: ].to_csv( str( os.getcwd() ) + "/Data0.csv", index = False, header = False, mode = "a" )
    elif file == "Data1.csv": 
        if len( data ) <= 3: # for beginning of run
            data.to_csv( str( os.getcwd() ) + "/Data1.csv", index = False ) 
        else: # for rest of run
            data.iloc[ -2: ].to_csv( str( os.getcwd() ) + "/Data1.csv", index = False, header = False, mode = "a" )
    elif file == "plotData.csv":
        runTime_current = data[ "Run Time" ].iloc[ -1 ]
        start = 0
        if runTime_current < config.plotRange: # for beginning of run
            # make array that allows a plot to be made because runTime[-1] - runTime[0] > plotRange (requirement in plotCode_data.py)
            makePlottable = [ [ data[ "Actual Time" ].iloc[ -1 ] - config.plotRange,
                                data[ "Run Time" ].iloc[ -1 ] - config.plotRange, 
                                dt.datetime.fromtimestamp( data[ "Date Time" ].iloc[ -1 ].timestamp() - config.plotRange ) ] ]
            for nColumn in range( 3, len( data.columns ) ):
                makePlottable[ 0 ].append( None )

            data.iloc[ 0:0 ].to_csv( config.plotDataPath, index = False ) # add column names to plotData.csv
            pd.DataFrame( makePlottable ).to_csv( config.plotDataPath, index = False, mode = "a", header = False ) # add makePlottable to plotData.csv
            data.iloc[ 1: ].to_csv( config.plotDataPath, index = False, mode = "a", header = False ) # add data to plotData.csv

        else: # for rest of run
            # walk backwards through data will in range of plotRange
            for nRow in range( len( data ) - 1, 0, -1 ):
                if data[ "Run Time" ][ nRow ] - runTime_current + config.plotRange > 0:
                    start = nRow
                else:
                    data[ start: ].to_csv( config.plotDataPath, index = False )
                    break

def updateSaveLocation( lastSaveFile ): # alternates save file
    if lastSaveFile == "Data0.csv": 
        return "Data1.csv"
    else: 
        return "Data0.csv"