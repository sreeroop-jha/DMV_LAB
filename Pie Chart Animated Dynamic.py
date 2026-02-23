import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.ion()
fig, ax = plt.subplots()
labels = ['A', 'B', 'C']

for i in range(10):
    sizes = np.random.randint(10, 50, size=3)
    ax.clear()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.pause(0.5)

plt.ioff()
plt.show()
