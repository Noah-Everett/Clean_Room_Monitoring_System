#============= Run Settings ==============#
runTime_total = 7 * 24 * 3600 # duration of run (seconds)
saveTime_data = 0 # time per data file save (seconds)
saveTime_plot = 2 # time per plotData.csv save (seconds)
dataTime = 0 # time per sensor data save (seconds)
autoStartRun = True # auto start new run at end of run
#============= Plot Settings =============#
plotRange = 600 # amount of time being graphed (seconds)

plotConfig = { "temperature": { "manualLimit": False, "yLower": 15,  "yUpper": 28,   "legend": True,  "logScale": False }, # library of plot configurations
               "humidity":    { "manualLimit": False, "yLower": 25,  "yUpper": 40,   "legend": True,  "logScale": False },
               "pressure":    { "manualLimit": False, "yLower": 25,  "yUpper": 40,   "legend": False, "logScale": False },
               "dust03":      { "manualLimit": False, "yLower": 1,   "yUpper": 100,                   "logScale": False },
               "dust05":      { "manualLimit": False, "yLower": 50,  "yUpper": 1000,                  "logScale": False },
               "voc":         { "manualLimit": False, "yLower": 1,   "yUpper": 400,                   "logScale": False },
               "co2":         { "manualLimit": False, "yLower": 350, "yUpper": 1800,                  "logScale": False } }
#=========================================#



dataTypes = [ "Actual Time", "Run Time", "Date Time", "Temperature_MS8607", # columns (data types) for csv data files (and database)
              "Temperature_DHT22", "Humidity_MS8607", "Humidity_DHT22", 
              "Pressure", "Dust_PM10Standard", "Dust_PM25Standard", 
              "Dust_PM100Standard", "Dust_PM10Env", "Dust_PM25Env", 
              "Dust_PM100Env", "Dust_Particles03um", "Dust_Particles05um", 
              "Dust_Particles10um", "Dust_Particles25um", "Dust_Particles50um", 
              "Dust_Particles100", "VolatileOrganicCompounds_eCO2", "VolatileOrganicCompounds_TVOC" ] 

dataDir = "/home/pi/MyRepos/crm/Data" # directory of where runs will be stored (crm/Data)
plotDataPath = "/home/pi/MyRepos/crm/Code/plotData.csv" # directory of where current plot data will be stored (crm/Code/plotData.csv)
