import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import miscCode

def initFig(): # initiate figure
    fig = plt.figure( figsize = ( 16, 9 ) )
    gs = gridspec.GridSpec( nrows = 5, ncols = 1 )

    return fig, gs
    
def plotAxis( ax, title, label, color, data, graphData, config ): # makes single axis for plot
    alpha = [ 1.0, 1.0 ]

    for n in range( len( graphData ) ):
        ax.plot( data[ "Actual Time" ] / 86400, data[ graphData[ n ] ], linewidth = 3, label = label[ n ], alpha = alpha[ n ], color = color[ n ] )
        ax.set_xlim( data[ "Actual Time" ][ 0 ] / 86400, data[ "Actual Time" ].iloc[ -1 ] / 86400 )

    if config[ "manualLimit" ]: 
        ax.set_ylim( config[ "yLower" ], config[ "yUpper" ] )
    if config[ "legend" ]: 
        ax.legend( loc = "upper right" )
    if config[ "logScale" ]: 
        ax.set_yscale( "log" )
        
    ax.set_ylabel( title, fontsize = 15 )
    ax.tick_params( axis = "both", labelsize = 10 )
    ax.grid()
    ax.xaxis_date( "MDT" )

def plotTwinAxis( ax, title, label, color, data, graphData, config ): # makes twin axis for plot
    alpha = [ 1.0, 1.0 ]
    line = []

    for n in [ 0, 1 ]:
        line.append( ax[ n ].plot( data[ "Actual Time" ] / 86400, data[ graphData[ n ] ], linewidth = 3, color = color[ n ], alpha = alpha[ n ] ) )
        ax[ n ].set_xlim( data[ "Actual Time" ][ 0 ] / 86400, data[ "Actual Time" ].iloc[ -1 ] / 86400 )

        if config[ n ][ "manualLimit" ]: 
            ax[ n ].set_ylim( config[ n ][ "yLower" ], config[ n ][ "yUpper" ] )
        if config[ n ][ "logScale" ]: 
            ax[ n ].set_yscale( "log" )

        ax[ n ].tick_params( axis = "y", labelsize = 10, labelcolor = color[ n ] )
        ax[ n ].grid()

    ax[ 0 ].tick_params( axis = "x", labelsize = 10 )
    ax[ 0 ].set_ylabel( title, fontsize = 15 )
    ax[ 0 ].legend( line[ 0 ] + line[ 1 ], [ label[ 0 ], label[ 1 ] ], loc = "upper right" )
    ax[ 1 ].legend( line[ 0 ] + line[ 1 ], [ label[ 0 ], label[ 1 ] ], loc = "upper right" )
    ax[ 0 ].xaxis_date( "MDT" )

def figConfig( fig ): # configures figure for plot
    fig.tight_layout()
    plt.pause( 0.001 )

def updateFig( fig, gs, data, plotConfig, runName ): # updates fugure for plot
    fig.clf()

    ax_temperature = fig.add_subplot( gs[ 0, 0 ] )
    plotAxis( ax_temperature, "Temperature [" + u"\N{DEGREE SIGN}C]", [ "MS8607", "DHT22" ], [ "gold" , "darkorange" ], data, [ "Temperature_MS8607", "Temperature_DHT22" ], plotConfig[ "temperature" ] )
    ax_temperature.set_title( runName + "   |   " + miscCode.printTime( int( data[ "Run Time" ].tail( 1 ) ) ) )
    plotAxis( fig.add_subplot( gs[ 1, 0 ] ), "Humidity [%]", [ "MS8607", "DHT22" ], [ "darkred", "crimson" ], data, [ "Humidity_MS8607", "Humidity_DHT22" ], plotConfig[ "humidity" ] )
    plotAxis( fig.add_subplot( gs[ 2, 0 ] ), "Pressure [Torr]", [ None ], [ "rebeccapurple" ], data, [ "Pressure" ], plotConfig[ "pressure" ] )
    ax_dust03 = fig.add_subplot( gs[ 3, 0 ] )
    plotTwinAxis( [ ax_dust03, ax_dust03.twinx() ], "Dust [Particles/L]", [ "≥0.3" + u"\u03bcm", "≥0.5" + u"\u03bcm" ], [ "mediumblue" , "teal" ], data, [ "Dust_Particles03um", "Dust_Particles05um" ], [ plotConfig[ "dust03" ], plotConfig[ "dust05" ] ] )
    ax_voc = fig.add_subplot( gs[ 4, 0 ] )
    plotTwinAxis( [ ax_voc, ax_voc.twinx() ], "Gas [ppb]", [ "Total VOC", "Equivalent CO2 / 1000" ], [ "darkslategray" , "limegreen" ], data, [ "VolatileOrganicCompounds_TVOC", "VolatileOrganicCompounds_eCO2" ], [ plotConfig[ "voc" ], plotConfig[ "co2" ] ] )

    figConfig( fig )