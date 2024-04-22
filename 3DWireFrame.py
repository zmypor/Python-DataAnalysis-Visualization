import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Create Canvas and Subplots
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the coordinates and shapes of Anime Images
x = np.linspace(-1, 1, 150)
y = np.linspace(-1, 1, 150)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x ** 2 + y ** 2))

# Define the Colors of Anime Images
colors = np.sin(np.arctan2(y, x))

# Adjust graphic perspective and display range
surf = ax.plot_surface(x, y, z, facecolors=cm.jet(colors), linewidth=0, antialiased=False)

# Adjust graphic perspective and display range
ax.view_init(elev=30, azim=45)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Display graphics
plt.show()
