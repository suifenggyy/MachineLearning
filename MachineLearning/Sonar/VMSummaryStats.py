import urllib.request
import sys
import numpy as np
import matplotlib.pylab as pylab
import scipy.stats as stats


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
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

stats.probplot(coldata, dist = "norm", plot = pylab)
pylab.show()