# **Clean Room Monitoring System (CRM)**

###### First, to properly view .md files, they need to be compiled. In git this is done automatically, but in VS Code this is done by right clicking on the file and selecting Open Preview.

This is the repo for the environmental monitoring of the SD Mines low-radon cleanroom. The following document will provide instructions on how to use the code as well as a brief explanation the main runable code files.

## **Running the Code**

First, follow the steps in `SETUP.md` to install all the required packages to the raspberry pi. 

Then using two terminal kernels, navigate to the directory of the `Code` folder in the repo in both kernels. Then run the following two lines, one in each terminal, in the respective order.

    python3 masterCode_data.py
    python3 masterCode_plot.py

`masterCode_data.py` will create a new `Run` folder within the `Data` folder and contains `Data0.csv` and `Data1.csv`. `masterCode_plot.py` produces a plot window that updates in real time. 

If a new run is started either manually or automatically, the plotting code (`masterCode_plot.py`) does not need to be restarted. It will automatically adjust to the new run.

## **Brief Explanation**

The code is split into two main files, `masterCode_data.py` and `masterCode_plot.py`. `masterCode_data.py` is responsible for reading data from all sensors and saving it to both `Data0.csv` and `Data1.csv` along with saving some data to `plotData.csv` which is used to display the plot of readings. `masterCode_plot.py` uses the data stored in `plotData.csv` to produce a plot of the newest data. Run settings for both programs can be found and changed in `config.py`.

`RunAnalysis.ipynb` can be used to quickly produce plots of entire runs along with minor data alaylsis which involves tweeking ranges of individual plots and changing the scale of the vertical axis. `DustAnalysis.ipynb` was used to compair dust readings between the PMSA003I and the Dylos DC1100. This file should not have to be used in the future.

## **Sensors**

Listed below is information on each of the four sensors in this system. The units provided for each type of data a sensor records are the default units the sensor outputs. Some of these are changed in the code which is represented by →. For example, by default the MS8607 outputs pressure in hPA, but in the code this is changed to Torr; this is represented by [hPa → Torr]. Also included for each sensor are two links. One is to the sensors product page on adafruit.com, the other is to it's tutorial/information page, which has been extremely helpful in the creation of this system.

- DHT22 - Temperature [℃] and humidity [%] sensor. [Product Page](https://www.adafruit.com/product/385) | [Tutorial](https://learn.adafruit.com/dht)

- MS8607 - Temperature [℃], pressure [hPa → Torr], and humidity [%]. [Product Page](https://www.adafruit.com/product/4716) | [Tutorial](https://learn.adafruit.com/adafruit-te-ms8607-pht-sensor)

- PMSA003I - Dust [particles/0.1L → particles/L] sensor. [Product Page](https://www.adafruit.com/product/4632) | [Tutorial](https://learn.adafruit.com/pmsa003i)

- SGP30 - Total volitile organic compounds [ppb] and equivalent calculated carbon-dioxide sensor [ppm → ppb]. [Product Page](https://www.adafruit.com/product/3709) | [Tutorial](https://learn.adafruit.com/adafruit-sgp30-gas-tvoc-eco2-mox-sensor)