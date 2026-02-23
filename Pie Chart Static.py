import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

labels = ['A', 'B', 'C']
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Static Pie Chart")
plt.show()
