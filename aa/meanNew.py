import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csvSize = 4521930
avgArr = []
data = pd.read_csv("out1.csv").to_numpy()
with open("consider.txt", "r") as f:
    for i in range(csvSize):
        line = f.readline()
        if line == '1\n':
            avgArr.append(data[i])

avgVal = sum([new[2] for new in avgArr])/np.shape(avgArr)[0]
print(avgVal)
