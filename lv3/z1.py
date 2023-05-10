import pandas as pd
import numpy as np

data = pd.read_csv('data_C02_emission.csv')

print('Mjerenja:',len(data))
print (data.info())
print(data.dtypes)
print ('Izostale vrijednosti:', data.isnull ().sum () )
print('Duplikati:',data.duplicated().sum())

data[['Make','Model','Vehicle Class','Transmission','Fuel Type']]=data[['Make','Model','Vehicle Class','Transmission','Fuel Type']].astype('category')


grouped=data.sort_values(ascending=[False],by='Fuel Consumption City (L/100km)')
print(grouped[['Make','Model','Fuel Consumption City (L/100km)']].head(3))
print(grouped[['Make','Model','Fuel Consumption City (L/100km)']].tail(3))

print('2.5 do 3.5L:',len(data[(data['Engine Size (L)']>=2.5)&(data['Engine Size (L)']<=3.5 )]))
print('AVG CO2:',data[(data['Engine Size (L)'] >=2.5)&(data['Engine Size (L)']<=3.5 )]['CO2 Emissions (g/km)'].mean())

print(len(data[(data['Make']=='Audi')])
print(data[(data['Make']=='Audi')&data['Cylinders']==4)]['CO2 Emissions (g/km)'].mean())

print(data.groupby(['Cylinders'])['CO2 Emissions (g/km)'].mean())

print(data[(data['Fuel Type'] == 'D')]['Fuel Consumption City (L/100km)'].mean())
print(data[(data['Fuel Type'] == 'X')]['Fuel Consumption City (L/100km)'].mean())
print(data[(data['Fuel Type'] == 'D')]['Fuel Consumption City (L/100km)'].median())
print(data[(data['Fuel Type'] == 'X')]['Fuel Consumption City (L/100km)'].median())

diesel_4cyl = data[(data['Cylinders'] == 4) & (data['Fuel Type'] == 'D')]
print(diesel_4cyl.sort_values(by = 'Fuel Consumption City (L/100km)').tail(1)[['Make','Model','Fuel Consumption City (L/100km)']])

print('Manuals:', len(data[data['Transmission'].str.startswith('M')]))

print(data.corr(numeric_only=True))
