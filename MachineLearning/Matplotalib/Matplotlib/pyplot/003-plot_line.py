import matplotlib.pyplot as plt

lines = plt.plot([4, 2, 3, 4])
plt.setp(lines, color='r', linewidth=2.0, alpha=0.5, animated=False)
plt.show()
