import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title("Static Scatter Plot")
plt.show()
