#import packages
import pandas as pd
import numpy as np

#to plot within notebook
import matplotlib.pyplot as plt


#setting figure size
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10

#for normalizing data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#read the file
df = pd.read_csv('EOD-MSFT.csv')

#print the head
print(df.head())

#setting index as date
df['Date']=pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index=df['Date']

#plot
plt.figure(figsize=(16,8))
plt.plot(df['Close'], label='Close Price history')

plt.show()