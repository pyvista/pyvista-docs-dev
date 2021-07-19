mesh = examples.load_hexbeam()

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_mesh(pv.PolyData(mesh.points), color='red',
            point_size=20, render_points_as_spheres=True)

pl.add_mesh(mesh.extract_cells(mesh.n_cells - 1), style='wireframe',
            color='blue', line_width=30, show_edges=True)

pl.camera_position = [(6.20, 3.00, 7.50),
                      (0.16, 0.13, 2.65),
                      (-0.28, 0.94, -0.21)]
pl.show()