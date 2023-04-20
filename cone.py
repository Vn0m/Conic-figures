import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

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
# ax.plot_surface(Xp, Yp, Zp, alpha=0.5, cmap='Blues')

# Find the intersection of the plane with the double cone
k = (2 * h) / (2 * h + 1)
Xe = k * Xp
Ye = k * Yp
Ze = Zp
ind = np.where((Xe**2 + Ye**2) < (h**2))
Xe = Xe[ind]
Ye = Ye[ind]
Ze = Ze[ind]


ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([1, 2*h])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()