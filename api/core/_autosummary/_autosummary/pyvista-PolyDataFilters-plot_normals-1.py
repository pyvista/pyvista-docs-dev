# Plot the normals of a sphere.
#
import pyvista as pv
sphere = pv.Sphere()
sphere.plot_normals(mag=0.1)
