# Animate plot as a wire-frame
plotter = pv.Plotter(window_size=(800, 600))
plotter.add_mesh(grid, scalars=d[:, 1],
                 show_scalar_bar=False,
                 rng=[-d.max(), d.max()], style='wireframe')
plotter.add_axes()
plotter.camera_position = cpos

#plotter.OpenMovie('beam_wireframe.mp4')
plotter.open_gif('beam_wireframe.gif')
for phase in np.linspace(0, 2*np.pi, 20):
    plotter.update_coordinates(grid.points + d*np.cos(phase), render=False)
    plotter.update_scalars(d[:, 1]*np.cos(phase), render=False)
    plotter.render()
    plotter.write_frame()

plotter.close()