import pylab

#this one isn't very impressive, and I don't think it is working right now anyway
#import src.interaction.timeSeries.simple
#src.interaction.timeSeries.simple.plot()
#pylab.plt.show()

import src.interaction.timeSeries.multicolorBars
src.interaction.timeSeries.multicolorBars.plot()
pylab.plt.show()

import src.PA.timeSeries.dailyMinutes
src.PA.timeSeries.dailyMinutes.plot()
pylab.plt.show()

import src.interaction_x_PA.scatterPlot
src.interaction_x_PA.scatterPlot.plot()
pylab.plt.show()
