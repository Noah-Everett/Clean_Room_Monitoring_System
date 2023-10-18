# **Cleanroom Monitoring System**

![SysteDiagram](https://github.com/Noah-Everett/Cleanroom_Monitoring_System/blob/main/CRM-Diagram.pdf)

This is the repository for the Cleanroom Monitoring System built to monitor the environment of the low radon cleanroom in the Dakota Building of South Dakota Mines. The following document will provide a summary of the system, instructions on how to use the code, and a brief explanation the main runnable code files.

## **Introduction**
The Cleanroom Monitoring System was created the Fall 2021 semester by me (Noah Everett), with guidance from Joseph Street (PhD student), for Dr. Richard Schnee's low radon cleanroom in the Dakota Building of South Dakota Mines. The system consists of a Raspberry Pi with four sensors (listed below) that record temperature, humidity, pressure, dust, carbon dioxide, and volatile organic compound levels. The purpose of the system was to allow cleanroom users to monitor how their actions affect the cleanroom environment in real time, along with recording data for future analysis.

Future use of the system may expand to include several other systems in other areas of the lab and/or other cleanrooms in the lab. The steps in `SETUP.md` can be followed to easily recreate the system as many times as desired. 

## **Sample Plot**
![Run007](https://github.com/Noah-Everett/Cleanroom_Monitoring_System/blob/main/Analysis/Runs/Run0007/Run0007%20Plot%20%5B2%5D.png)

## **Running the Code**

First, follow the steps in `SETUP.md` to install all the required packages to the Raspberry Pi. 

Next, using two terminal kernels, navigate to the directory of the `Code` folder in the repo in both kernels. Then, run the following two lines, one in each terminal, in the respective order.

    python3 masterCode_data.py
    python3 masterCode_plot.py

`masterCode_data.py` will create a new `Run` folder within the `Data` directory that contains `Data0.csv` and `Data1.csv`. `masterCode_plot.py` produces a plot window that updates in real time. 

If a new run is started either manually or automatically, the plotting code (`masterCode_plot.py`) does not need to be restarted. It will automatically adjust to the new run.

## **Brief Explanation**

The main code (in `Code/`) is split into two main files, `masterCode_data.py` and `masterCode_plot.py`. `masterCode_data.py` is responsible for reading data from all sensors and alternating between saving it to both `Data0.csv` and `Data1.csv` along with saving the most recent data to `plotData.csv`. `masterCode_plot.py` uses the data stored in `plotData.csv` to produce a plot of the newest data. Run settings for both programs can be found and changed in `config.py`.

`RunAnalysis.ipynb` (in `Analysis/Code/`) can be used to quickly produce plots of entire runs along with minor data analysis which involves tweaking ranges of individual plots and changing the scale of the vertical axis. `DustAnalysis.ipynb` (also in `Analysis/Code/`) was used to compare dust readings between PMSA003I and Dylos DC1100 dust sensors. This file should not have to be used in the future.

## **Sensors**

Information on each of the four sensors in this system is listed below. The units provided for each type of measurement a sensor records are the default units the sensor outputs. Some of these are changed in the code which is represented by →. For example, by default the MS8607 outputs pressure in hPa, but in the code this is changed to Torr; this is represented by [hPa → Torr]. Also included for each sensor are two links. One is to the sensors product page on adafruit.com, the other is to its tutorial/information page, which has been extremely helpful in the creation of this system.

- DHT22 - Temperature [℃] and humidity [%] sensor. [Product Page](https://www.adafruit.com/product/385) | [Tutorial](https://learn.adafruit.com/dht)

- MS8607 - Temperature [℃], pressure [hPa → Torr], and humidity [%]. [Product Page](https://www.adafruit.com/product/4716) | [Tutorial](https://learn.adafruit.com/adafruit-te-ms8607-pht-sensor)

- PMSA003I - Dust [particles/0.1L → particles/L] sensor. [Product Page](https://www.adafruit.com/product/4632) | [Tutorial](https://learn.adafruit.com/pmsa003i)

- SGP30 - Total volatile organic compounds [ppb] and equivalent calculated carbon-dioxide sensor [ppm → ppb]. [Product Page](https://www.adafruit.com/product/3709) | [Tutorial](https://learn.adafruit.com/adafruit-sgp30-gas-tvoc-eco2-mox-sensor)
