import time

import dataCode_data as dataCode
import config

def main(): # main function for data handling; gets and saves data to run file and plotData.csv
        dataCode.makeDataFiles()

        data = dataCode.initDataFrame()

        runTime_current = 0.0
        runTime_start = time.time()
        saveFile = "Data0.csv"

        numFileSaves = 0
        numDataSaves = 0
        numPlotDataSaves = 0

        data = dataCode.updateData( data, runTime_current )

        while runTime_current <= config.runTime_total:
            runTime_current = time.time() - runTime_start
            
            # gets data from sensors at frequency of dataTime
            if runTime_current > numDataSaves * config.dataTime: 
                data = dataCode.updateData( data, runTime_current )
                numDataSaves += 1
            
            # saves recent data to plotData.csv at frequency of saveTime_plot
            if runTime_current > numPlotDataSaves * config.saveTime_plot: 
                dataCode.updateFile( data, "plotData.csv" )
                numPlotDataSaves += 1

            # saves data to alternating csv file at frequency of saveTime_plot
            if runTime_current > numFileSaves * config.saveTime_data:
                saveFile = dataCode.updateSaveLocation( saveFile )
                dataCode.updateFile( data, saveFile )
                numFileSaves += 1

        # auto start run
        if config.autoStartRun: 
            main()

main()