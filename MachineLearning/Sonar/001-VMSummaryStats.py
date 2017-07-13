import urllib.request

import matplotlib.pylab as pylab
import pandas
import scipy.stats as stats

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar"
              "/sonar.all-data")
rocksVMines = pandas.read_csv(target_url, header=None, prefix="V")

print(rocksVMines.head())
print(rocksVMines.tail())

summary = rocksVMines.describe()
print(summary)

data = urllib.request.urlopen(target_url)

xList = []
labels = []

for line in data:
    row = line.decode().strip().split(",")
    xList.append(row)

nrow = len(xList)
ncol = len(xList[0])
type = [0] * 3
colCounts = []

col = 3
coldata = []

for row in xList:
    coldata.append(float(row[col]))

stats.probplot(coldata, dist="norm", plot=pylab)
pylab.show()


