import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.arange(0, 10)
y = np.zeros(10)
line, = ax.plot(x, y)

def update(frame):
    line.set_ydata(np.random.randint(0, 50, size=10))
    return line,

ani = FuncAnimation(fig, update, frames=20, interval=500)
plt.show()
