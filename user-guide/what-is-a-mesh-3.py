import pyvista as pv
from pyvista import examples
mesh = examples.download_bunny_coarse()

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_mesh(pv.PolyData(mesh.points), color='red',
            point_size=10, render_points_as_spheres=True)
pl.camera_position = [(0.02, 0.30, 0.73),
                      (0.02, 0.03, -0.022),
                      (-0.03, 0.94, -0.34)]
pl.show()