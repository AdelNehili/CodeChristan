import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#numpy allows to work with arrays
#matplotlib allows to plot graphs
#pandas allows to work with dataframes


# Read the csv file
df = pd.read_csv('site.csv', header=None, parse_dates=[0], delimiter=',')

print(df.head(15))
# Rename columns for better understanding
df.columns = ['C0', 'C1', 'C2', 'C3']
print(df['C1'].dtype)


# Calculate the mean using numpy
#mean_value1 = np.mean(df['C1'])

# Print the mean values
#print(f'Mean of Value1: {mean_value1}')