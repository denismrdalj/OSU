import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd . read_csv ('data_C02_emission.csv')

plt.figure()
data['CO2 Emissions (g/km)'].plot(kind='hist',bins=30)
plt.show()

colors = { 'X': 'blue', 'Z': 'green', 'D': 'red', 'E': 'orange', 'N': 'black' }
data.plot.scatter(x='Fuel Consumption City (L/100km)',y='CO2 Emissions (g/km)',c=data['Fuel Type'].apply(lambda x: colors[x]), cmap ="hot", s=10)
plt.show()

grouped = data.groupby('Fuel Type')
data.boxplot(column=['Fuel Consumption Hwy (L/100km)'], by='Fuel Type')

plt.figure()
plt.subplot(111)
data.groupby('Fuel Type').size().plot(kind = 'bar')

plt.subplot(112)
data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean().plot(kind = 'bar')
plt.show()






