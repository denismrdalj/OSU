import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score



#1A
data = pd.read_csv('data_C02_emission.csv')
print('Mjerenja:',len(data))
print(data.columns.tolist())
print(data)

#1B
data[['Make','Model','Vehicle Class','Transmission','Fuel Type']]=data[['Make','Model','Vehicle Class','Transmission','Fuel Type']].astype('category')
plt.figure()
sns.barplot(data=data, y=data['Fuel Consumption City (L/100km)'],x=data['Cylinders'])
plt.show()

#1C
print(len(data[(data['Fuel Consumption City (L/100km)']>8.0)]))

print(len(data[(data['Fuel Consumption City (L/100km)']<=8.0)]))

#1D
print(data.corr(numeric_only=True))


#2A
y = data['CO2 Emissions (g/km)']
X = data[['Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)',
          'Fuel Consumption Comb (L/100km)', 'Engine Size (L)', 'Fuel Consumption Comb (mpg)', 'Cylinders']]

data['CO2 Emissions (g/km)'] = np.where(data['CO2 Emissions (g/km)'] > 245,1,0)

print(data)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

sc = MinMaxScaler()
X_train_n = sc.fit_transform( X_train )
X_test_n = sc.transform( X_test )

linearModel = lm.LinearRegression ()
linearModel.fit(X_train_n, y_train)
print(linearModel.coef_)

y_test_predict = linearModel.predict(X_test_n)
plt.scatter(y_test_predict, y_test, c='red' )
plt.show()

MAE = mean_absolute_error(y_test, y_test_predict)
MAPE = mean_absolute_percentage_error(y_test, y_test_predict)
MSE = mean_squared_error(y_test, y_test_predict)
R2 = r2_score(y_test, y_test_predict)

print("Srednja apsolutna pogreška iznosi", round(MAE, 2))
print("Srednja apsolutna postotna pogreška iznosi", round(MAPE, 2))
print("Srednja kvadratna pogreška iznosi", round(MSE, 2))
print("Koeficijent determinacije (R2) iznosi", round(R2, 2))


