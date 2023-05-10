import pandas as pd
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

y = data['CO2 Emissions (g/km)']
X = data[['Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)',
          'Fuel Consumption Comb (L/100km)', 'Engine Size (L)', 'Fuel Consumption Comb (mpg)', 'Cylinders']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

plt.scatter(X_train['Fuel Consumption City (L/100km)'], y_train, c='blue', s=2)
plt.scatter(X_test['Fuel Consumption City (L/100km)'], y_test, c='red', s=2)
plt.legend(['Training data', 'Test data'])
plt.show()

sc = MinMaxScaler()
X_train_n = sc.fit_transform( X_train )
X_test_n = sc.transform( X_test )
plt.hist(X_train["Fuel Consumption City (L/100km)"], bins=15, color="red")
plt.title('Pre scale')
plt.show()
plt.hist(X_train_n[0], bins=15, color="orange")
plt.title('Post scale')
plt.show()

linearModel = lm.LinearRegression ()
linearModel.fit(X_train_n, y_train)
print(linearModel.coef_)

y_test_predict = linearModel.predict(X_test_n)
plt.scatter(y_test_predict, y_test, c='red' )

MSE = skmetrics.mean_squared_error(y_test, y_test_predict)
print("Test size: 0.2")
print("MSE: ", MSE)
print("RMSE: ", math.sqrt(MSE))
print("MAE: ", skmetrics.mean_absolute_error(y_test, y_test_predict))
print("MAPE: ", skmetrics.mean_absolute_percentage_error(y_test, y_test_predict))
print("Rsquared: ", skmetrics.r2_score(y_test, y_test_predict))






