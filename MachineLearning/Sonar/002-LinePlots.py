import matplotlib.pyplot as plot
import pandas as pd

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar"
              "/sonar.all-data")
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

for i in range(208):
    if rocksVMines.iat[i, 60] == 'M':
        pcolor = "red"
    else:
        pcolor = "blue"
    datarow = rocksVMines.iloc[i, 0:60]
    datarow.plot(color=pcolor)

plot.xlabel("Attr Index")
plot.ylabel(("Attr value"))
plot.show()

