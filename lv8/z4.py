import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score
from sklearn.cluster import KMeans

iris=sns.load_dataset('iris')
versicolor = iris[(iris['species']=='versicolor')]
virginica = iris[(iris['species']=='virginica')]
setosa = iris[(iris['species']=='setosa')]
joined=pd.concat([versicolor,virginica])
sns.scatterplot(data=joined,x='petal_length',y='sepal_length',hue='species')
plt.show()

versi_avg = versicolor['sepal_width'].mean()
virgi_avg = virginica['sepal_width'].mean()
setos_avg = setosa['sepal_width'].mean()
versicolor['average'] = versi_avg
virginica['average'] = virgi_avg
setosa['average'] = setos_avg
joined=pd.concat([versicolor,virginica,setosa])
sns.barplot(data=joined,x=joined['species'],y=joined['average'])
plt.show()

print(len(virginica[(virginica['sepal_width']>virgi_avg)]))


#2
features=['petal_length','sepal_length']
prepped = iris[features].copy()
ssd=[]
K = range(1,10)
for num_clusters in K:
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(prepped)
    ssd.append(kmeans.inertia_)
plt.plot(K,ssd,'bx-')
plt.show()

scaler=StandardScaler()
scaled_iris = scaler.fit_transform(prepped)

model = KMeans(init='random',n_clusters=3)
model.fit(prepped)
centroids = model.cluster_centers_
labels=model.labels_
sns.scatterplot(x=prepped.iloc[:,0],y=prepped.iloc[:,1],hue=labels)
plt.scatter(centroids[:,0],centroids[:,1],marker='*')
plt.show()





