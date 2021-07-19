# Store Camera position.  This can be obtained manually by getting the
# output of grid.plot()
# it's hard-coded in this example
cpos = [(11.915126303095157, 6.11392754955802, 3.6124956735471914),
        (0.0, 0.375, 2.0),
        (-0.42546442225230097, 0.9024244135964158, -0.06789847673314177)]

# plot this displaced beam
plotter = pv.Plotter()
plotter.add_mesh(grid, scalars=d[:, 1],
                 scalar_bar_args={'title': 'Y Displacement'},
                 rng=[-d.max(), d.max()])
plotter.add_axes()
plotter.camera_position = cpos
plotter.show()