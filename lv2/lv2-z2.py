import numpy as np
import matplotlib.pyplot as plt
array=np.loadtxt("data.csv", delimiter=",",skiprows=1)
print(array)
#a
persons=len(array)
print (persons)
#b,c
heights=[]
weights=[]
for i in range(0,len(array),50):
        heights.append(array[i][1])
        weights.append(array[i][2])
heights.sort()
weights.sort()
plt.plot(heights,weights,'b')
plt.scatter(heights,weights)
plt.show()
#d
h=[]
for i in range(0,len(array)):
        h.append(array[i][1])
print("Average: ",np.average(h))
print("Min: ",np.min(h))
print("Max",np.max(h))
#e
h1=[]
h0=[]
for i in range(0,len(array)):
        if(array[i][0]==1):
            h1.append(array[i][1])
        if(array[i][0]==0):
            h0.append(array[i][1])
print("Average1: ",np.average(h1))
print("Min1: ",np.min(h1))
print("Max1",np.max(h1))
print("Average0: ",np.average(h0))
print("Min0: ",np.min(h0))
print("Max0",np.max(h0))
