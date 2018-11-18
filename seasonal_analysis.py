import pandas
import numpy as np
import matplotlib.pyplot as plt
import util
import time_series_analysis as ts
import os
from scipy.fftpack import fft


#set the value of the bin
std_bin_size = 60*60*24

##get the data
os.chdir(r"C:\Users\REMY\Documents\5. Coding\Hackatons\2018 AI Hack\Data\Road Accident")
data = util.read_with_timestamps("Road-Accident.csv")

##set path to folder for timestamps
os.chdir(r"C:\Users\REMY\Documents\GitHub\ai-hack18")

## plotting
x, y = ts.histogram(data, "age_of_driver", value=36)




