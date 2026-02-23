import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
labels = ['A', 'B', 'C']

def update(frame):
    ax.clear()
    sizes = np.random.randint(10, 50, size=3)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')

ani = FuncAnimation(fig, update, frames=20, interval=500)
plt.show()
