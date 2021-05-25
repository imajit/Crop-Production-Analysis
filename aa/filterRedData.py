import pandas as pd
import numpy as np
finarr = []
consider = []
filename = "filterOut.csv"
myData = pd.read_csv(filename).to_numpy()
for row in myData:
    if 0.07 <= row[2] <= 0.25:
        finarr.append(row)
        consider.append(1)
    else:
        consider.append(0)

print(np.shape(finarr))

with open("consider.txt", "w") as f:
    for item in consider:
        f.write("%s\n" % item)
