mesh.cell_arrays['my cell values'] = np.arange(mesh.n_cells)
mesh.plot(scalars='my cell values', cpos=cpos, show_edges=True)