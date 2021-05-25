import numpy as np
finarr = []
threshold = 0.5
with open("diff.txt", "r") as f:
    line = f.readline()
    if line == "None\n":
        finarr.append(None)
    else:
        line = line[:-2]
        finarr.append(float(line))
    while True:
        line = f.readline()
        if line == "\n" or line == "":
            break
        if line == "None\n" or line == "\n":
            finarr.append(None)
        else:
            line = line[:-2]
            finarr.append(float(line))
proppixel = []
for j in finarr:
    if j is not None:
        proppixel.append(j)
filteredarr = []
for j in proppixel:
    if j > threshold:
        filteredarr.append(j)
print(np.shape(filteredarr))


