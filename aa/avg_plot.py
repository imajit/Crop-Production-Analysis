import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
vegpercarr = []
avgndvi = []
for i in range(1, 25):
    filename = "out" + str(i) + ".csv"
    data = pd.read_csv(filename).to_numpy()
    newarr = []
    for row in data:
        row[2] = 0-row[2]
    for row in data:
        if row[2] >= -1 and row[2] <= 1:
            newarr.append(row)
    avgndv = sum([new[2] for new in newarr])/np.shape(newarr)[0]
    avgndvi.append(avgndv)

x = [i for i in range(1, 25)]
y = avgndvi[:]
plt.plot(x, y)
plt.show()
plt.savefig("avg_plot.png")
