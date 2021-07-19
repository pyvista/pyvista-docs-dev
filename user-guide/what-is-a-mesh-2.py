import pyvista as pv
import numpy as np
from pyvista import examples

mesh = examples.load_hexbeam()
cpos = [(6.20, 3.00, 7.50),
        (0.16, 0.13, 2.65),
        (-0.28, 0.94, -0.21)]

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_mesh(pv.PolyData(mesh.points), color='red',
       point_size=10, render_points_as_spheres=True)
pl.camera_position = cpos
pl.show()