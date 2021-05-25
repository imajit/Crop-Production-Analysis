print("Importing library")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Loading file ")
file_path = 'results.csv'
print ('Loaded Data')
data = pd.read_csv(file_path,header = None)
data1 = []
data2 = []
data = np.array(data)
#data.values.reshape([98,1])
#data.shape()
for i in range(49):
	data1.append(data[i*2])
for i in range(49):
	data2.append(data[1+i*2,0])
#plt.plot(data1,'r')
plt.plot(data2,'g')
plt.show()
