import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.ion()
fig, ax = plt.subplots()

for i in range(10):
    x = np.random.rand(50)
    y = np.random.rand(50)
    ax.clear()
    ax.scatter(x, y)
    plt.pause(0.5)

plt.ioff()
plt.show()
