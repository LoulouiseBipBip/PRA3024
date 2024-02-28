# -*- coding: utf-8 -*-
"""Challenge1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/122SVaug4ZCGrHjDsCSLi6nEnBkuz6Dw1
"""

from gwosc.datasets import find_datasets
from gwosc import datasets
from gwosc.datasets import event_gps
from gwpy.timeseries import TimeSeries

#GEtting the data in Time series
T = TimeSeries.read('challenge1.gwf', channel="H1:CHALLENGE1")
print("The sampling rate is")
print(T.dt)

print("The duration of the data is:")
print(T.duration)

#Time plot
T.plot()
plot.show()

hq = T.q_transform(frange=(30, 300), qrange=(30, 50), outseg=(0,+4))
plot = hq.plot()
plot.colorbar(label="Normalised energy")
ax = plot.gca()
ax.set_yscale("log")
plot.show  # refresh



