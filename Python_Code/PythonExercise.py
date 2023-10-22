import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('PowerCurve.csv', sep = ';', header = None)
print(df)

matrix = df.to_numpy()
print(matrix)

V = matrix[:,0]
P = matrix[:,1]
plt.plot(V,P)
plt.xlabel('Wind speed [m/s]')
plt.ylabel('Power [W]')
plt.grid(b=True, which = 'both')
plt.show()
