# Create a default plane.
#
import pyvista
mesh = pyvista.Plane()
mesh.point_arrays.clear()
mesh.plot(show_edges=True)
