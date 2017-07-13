import matplotlib.pyplot as plt
import numpy as np

plt.plot([3, 4, 5, 6])

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

plt.axis([0, 6, 0, 20])

t = np.arange(0., 5., 0.1)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()
