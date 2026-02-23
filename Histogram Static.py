import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.title("Static Histogram")
plt.show()
