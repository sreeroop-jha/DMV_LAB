import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = ['A', 'B', 'C', 'D']
y = [10, 20, 30, 40]

plt.ion()
fig, ax = plt.subplots()
bars = ax.bar(x, y)

for i in range(10):
    new_y = np.random.randint(5, 50, size=4)
    for bar, val in zip(bars, new_y):
        bar.set_height(val)
    plt.pause(10)

plt.ioff()
plt.show()
