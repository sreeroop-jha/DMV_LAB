import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig,ax = plt.subplots()
ax.set_xlim(0,10)
ax.set_ylim(0,10)
circle = plt.Circle((0,5), 0.5, color = 'blue')
ax.add_patch(circle)
def update(frame):
    x = frame
    circle.center = (x,5)
    return circle,
ani = FuncAnimation(fig, update , frames =100, interval = 50)
plt.show()
