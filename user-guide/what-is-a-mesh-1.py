import numpy as np
import pyvista as pv

nodes = np.random.rand(100, 3)
mesh = pv.PolyData(nodes)
mesh.plot(point_size=30, render_points_as_spheres=True)