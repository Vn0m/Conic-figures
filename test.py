import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define cone parameters
r = 1
h = 2

# Define the surfaces of the cones
u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(0, h, 30)
U, V = np.meshgrid(u, v)

X1 = r * (1 - V/h) * np.cos(U)
Y1 = r * (1 - V/h) * np.sin(U)
Z1 = V

X2 = r * (1 - V/h) * np.cos(U)
Y2 = r * (1 - V/h) * np.sin(U)
Z2 = 2*h - V

# Combine the surfaces into a single plot
X = np.concatenate((X1, X2))
Y = np.concatenate((Y1, Y2))
Z = np.concatenate((Z1, Z2))
ax.plot_surface(X, Y, Z, cmap='viridis')

# Define the surface of the plane
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
Xp, Yp = np.meshgrid(x, y)
Zp = Xp + Yp + 2

# Plot the plane
ax.plot_surface(Xp, Yp, Zp, alpha=0.5, cmap='Blues')

# Find the intersection of the plane with the double cone
k = (2 * h) / (2 * h + 1)
Xe = k * Xp
Ye = k * Yp
Ze = Zp
ind = np.where((Xe**2 + Ye**2) < (h**2))
Xe = Xe[ind]
Ye = Ye[ind]
Ze = Ze[ind]

# Plot the intersection curve as an ellipse and a parabola
ellipse = ax.plot(Xe, Ye, Ze-Ye-0.4, color='r', label='ellipse')
parabola = ax.plot(Xe, Ye, Ze-Xe-Ye-0.6, color='orange', label='parabola')

# Define the circle
theta = np.linspace(0, 2*np.pi, 100)
xc = 0.8 * np.sqrt(h**0.8) * np.cos(theta)  # smaller radius
yc = 0.8 * np.sqrt(h**0.8) * np.sin(theta)  # smaller radius
zc = np.ones_like(theta) + 1.2*h        # shift z-axis up by 1.2*h

# Plot the circle
circle, = ax.plot(xc, yc, zc, color='blue', linewidth=2, zorder=10, label='circle')
circle.set_color('blue')

# Set axis limits and labels
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([1, 2*h])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add legend
ax.legend()

# Show the plot
plt.show()