import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(0, 10)
y = x ** 2

plt.plot(x, y)
plt.title("Static Line Chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
