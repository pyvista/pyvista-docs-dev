plotter = pv.Plotter(window_size=(800, 600))
plotter.add_mesh(grid, scalars=d[:, 1],
                 show_scalar_bar=False,
                 show_edges=True, rng=[-d.max(), d.max()])
plotter.add_axes()
plotter.camera_position = cpos

# open movie file.  A mp4 file can be written instead.  Requires ``moviepy``
plotter.open_gif('beam.gif')  # or beam.mp4

# Modify position of the beam cyclically
pts = grid.points.copy()  # unmodified points
for phase in np.linspace(0, 2*np.pi, 20):
    plotter.update_coordinates(pts + d*np.cos(phase))
    plotter.update_scalars(d[:, 1]*np.cos(phase))
    plotter.write_frame()

# Close the movie and plot
plotter.close()