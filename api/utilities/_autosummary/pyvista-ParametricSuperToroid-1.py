# Create a ParametricSuperToroid mesh
#
import pyvista
mesh = pyvista.ParametricSuperToroid()
mesh.plot(color='w', smooth_shading=True)
