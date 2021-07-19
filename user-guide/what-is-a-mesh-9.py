cube = pv.Cube().clean()
cube.point_arrays['myscalars'] = range(8)
cube.plot(cmap='bwr')