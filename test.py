import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create the data for the plot
x = np.arange(1, 10)
y = np.arange(1, 10)
x, y = np.meshgrid(x, y)

z = x + y
z = z.astype(float)
# Filter out values that don't satisfy the condition x + y <= 10
z[x + y > 10] = np.nan

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

# Set the labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D plot of x + y = z')

# Show the plot
plt.show()
