import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.ion()
fig, ax = plt.subplots()
x = np.arange(0, 10)
y = np.zeros(10)
line, = ax.plot(x, y)

for i in range(20):
    y = np.random.randint(0, 50, size=10)
    line.set_ydata(y)
    plt.pause(0.5)

plt.ioff()
plt.show()
