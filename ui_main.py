import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

with open('djer.csv', newline='') as f:
 reader = csv.reader(f)
 data = list(reader)

np.array(data, dtype=float)
print(np.array(data, dtype=float))
#z = np.array(data, dtype=float)

x,y,z = np.loadtxt("data.txt", unpack=True)
#plt.contourf(z, levels=[11, 12, 13],
#    colors=['#808080', '#A0A0A0', '#C0C0C0'], extend='both')
plt.contour(x.reshape(9,3), y.reshape(4,3), z.reshape(4,3))
plt.show()
