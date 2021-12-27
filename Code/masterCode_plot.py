import config
import dataCode_plot as dataCode
import plotCode

def main(): # main function for plotting; gets data and updates plot
    fig, gs = plotCode.initFig()

    # update plot
    while True:
        runName = dataCode.getRunName()
        data = dataCode.getData( config.plotDataPath )
        plotCode.updateFig( fig, gs, data, config.plotConfig, runName )

main()