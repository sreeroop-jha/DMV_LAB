import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.ion()
fig, ax = plt.subplots()

for i in range(10):
    data = np.random.randn(1000)
    ax.clear()
    ax.hist(data, bins=30)
    plt.pause(0.5)

plt.ioff()
plt.show()
