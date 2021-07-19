mesh.point_arrays['my point values'] = np.arange(mesh.n_points)
mesh.plot(scalars='my point values', cpos=cpos, show_edges=True)