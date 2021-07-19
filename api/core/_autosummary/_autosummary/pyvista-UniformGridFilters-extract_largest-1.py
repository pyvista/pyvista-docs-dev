# Join two meshes together, extract the largest, and plot it.
#
import pyvista
mesh = pyvista.Sphere() + pyvista.Cube()
largest = mesh.extract_largest()
largest.point_arrays.clear()
largest.cell_arrays.clear()
largest.plot()
