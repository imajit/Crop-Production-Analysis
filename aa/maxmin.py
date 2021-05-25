import pandas as pd
import numpy as np
csvsize = 4521930
vegpercarr = []
maxarr = [-1 for i in range(csvsize)]
minarr = [1 for i in range(csvsize)]
x = pd.read_csv("out1.csv")
for i in range(1, 25):
    filename = "out" + str(i) + ".csv"
    data = pd.read_csv(filename).to_numpy()
    for j in range(csvsize):
        data[j][2] = 0-data[j][2]
    for j in range(csvsize):
        if maxarr[j] is None and minarr[j] is None:
            continue
        if data[j][2] < -1 or data[j][2] > 1:
            maxarr[j] = None
            minarr[j] = None
            continue
        maxarr[j] = max(maxarr[j], data[j][2])
        minarr[j] = min(minarr[j], data[j][2])
diffarr = []
for i in range(csvsize):
    if maxarr[i] is None:
        diffarr.append(None)
        continue
    diffarr.append(maxarr[i]-minarr[i])

with open("diff.txt", "w") as f:
    for item in diffarr:
        if item is None:
            f.write("None\n")
        else:
            f.write("%s\n" % item)
