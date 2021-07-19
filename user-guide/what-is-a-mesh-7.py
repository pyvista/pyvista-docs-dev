mesh = examples.load_uniform()

pl = pv.Plotter(shape=(1,2))
pl.add_mesh(mesh, scalars='Spatial Point Data', show_edges=True)
pl.subplot(0,1)
pl.add_mesh(mesh, scalars='Spatial Cell Data', show_edges=True)
pl.show()