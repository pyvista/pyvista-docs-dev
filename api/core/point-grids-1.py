import pyvista as pv
import numpy as np

x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
z = np.arange(-10, 10, 0.25)
x, y, z = np.meshgrid(x, y, z)

# create the unstructured grid directly from the numpy arrays and plot
grid = pv.StructuredGrid(x, y, z)
grid.plot(show_edges=True)