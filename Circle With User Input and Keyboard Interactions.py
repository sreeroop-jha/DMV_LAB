import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = int(input("Enter number of frames: "))
speed = float(input("Enter speed:"))

fig, ax = plt.subplots()
ax.set_xlim(0,10)
ax.set_ylim(0,10)

circle = plt.Circle((5,5), 0.5, color = 'blue')
ax.add_patch(circle)
dx, dy = 0, 0

def on_key(event):
    global dx, dy

    if event.key == 'w' or event.key == 'up':
        dx ,  dy = 0 , speed
    elif event.key == 's' or event.key == 'down':
        dx , dy = 0, -speed
    elif event.key == 'a' or event.key == 'left':
        dx , dy = -speed , 0
    elif event.key == 'd' or event.key == 'right':
        dx, dy = speed ,0
    elif event.key == ' ' :
        dx, dy = 0, 0

fig.canvas.mpl_connect('key_press_event', on_key)
def update(frame):
    x, y = circle.center
    new_x = x+ dx * 0.1
    new_y = y + dy * 0.1
    new_x = max(0, min(10, new_x))
    new_y = max(0, min(10, new_y))
    circle.center = (new_x, new_y)
    return circle,
ani = FuncAnimation(fig, update, frames = frames, interval = 50)
plt.show()
        
