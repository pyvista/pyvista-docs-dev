# Create a ParametricSuperEllipsoid mesh
#
import pyvista
mesh = pyvista.ParametricSuperEllipsoid()
mesh.plot(color='w', smooth_shading=True)
