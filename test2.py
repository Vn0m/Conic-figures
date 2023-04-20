import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the base radius and height of the cones
r = 1
h = 2

# Define the angle for the double cone
theta = np.linspace(0, 2*np.pi, 100)

# Define the x and y coordinates for the base circles
x1 = r*np.cos(theta)
y1 = r*np.sin(theta)
x2 = -r*np.cos(theta)
y2 = -r*np.sin(theta)

# Define the z coordinates for the top and bottom of each cone
z1_top = h*np.ones_like(theta)
z1_bottom = np.zeros_like(theta)
z2_top = -h*np.ones_like(theta)
z2_bottom = np.zeros_like(theta)

# Plot the top and bottom circles for each cone
ax.plot(x1, y1, z1_top, color='blue')
ax.plot(x1, y1, z1_bottom, color='blue')
ax.plot(x2, y2, z2_top, color='blue')
ax.plot(x2, y2, z2_bottom, color='blue')

# Plot the lines connecting the top and bottom of each cone
for i in range(len(theta)):
    ax.plot([x1[i], 0, x2[i]], [y1[i], 0, y2[i]], [z1_top[i], z1_bottom[i], z2_top[i]], color='blue')

plt.show()


