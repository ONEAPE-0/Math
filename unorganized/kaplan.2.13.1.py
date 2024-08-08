#Goal is to plot a space curve, find the equation of tangent line across a point and then find the perpindicular plane.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter t
t = np.linspace(0, 2 * np.pi, 400)

# Parametric equations
x = np.sin(t)
y = np.cos(t)
z = np.sin(t)**2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the curve
ax.plot(x, y, z, label='x = sin(t), y = cos(t), z = sin^2(t)')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Parametric Curve')
ax.legend()

# Enhance the plot
ax.grid(True)
ax.view_init(elev=30, azim=30)  # Adjust viewing angle if necessary

plt.show()
