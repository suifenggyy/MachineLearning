import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-1, 2, .002)
s = np.sin(2 * np.pi * t)
m = t
plt.plot(t, s)
plt.plot(t, m)

# draw a thick red hline at y=0 that spans the xrange
plt.axhline(y=0, linewidth=2, color='r')
plt.axvline(x=0, ymin=0.5, linewidth=2, color='b')

plt.axis([-1, 2, -1, 2])
plt.show()
