import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = ['A', 'B', 'C', 'D']
y = [10, 24, 36, 18]

plt.bar(x, y)
plt.title("Static Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
