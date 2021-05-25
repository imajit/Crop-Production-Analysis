import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
vegpercarr = []
avgndvi = []
for i in range(1, 25):
    filename = "out" + str(i) + ".csv"
    data = pd.read_csv(filename).to_numpy()
    vegetation = []
    avndvi = sum( cvb := list(filter(lambda x: x >= -1 and x <= 1, [dat[2] for dat in data])))/np.shape(cvb)
    for row in data:
        if row[2] <= -0.2 and row[2] >= -0.5:
            vegetation.append(row)
    vegperc = (np.shape(vegetation)[0] / np.shape(data)[0]) * 100
    vegpercarr.append(vegperc)

x = [i for i in range(1, 25)]
y = vegpercarr[:]
plt.plot(x, y)
plt.show()
