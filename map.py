import pandas as pd


data = pd.read_csv("djer_small.csv", sep=",", header=None)
print(data)
data.columns = ["Lat", "Lon", "Depth"]



import numpy as np
X = np.array(data.Lat.values)
Y = np.array(data.Lon.values)
Z = np.array(data.Depth.values)


xinum = (max(X) - min(X))
print(xinum)