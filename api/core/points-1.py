import pyvista
from pyvista import examples

# load and shrink airplane
airplane = pyvista.PolyData(examples.planefile)
airplane.points /= 10 # shrink by 10x

# rotate and translate ant so it is on the plane
ant = pyvista.PolyData(examples.antfile)
ant.rotate_x(90)
ant.translate([90, 60, 15])

# Make a copy and add another ant
ant_copy = ant.copy()
ant_copy.translate([30, 0, -10])

# Create plotting object
plotter = pyvista.Plotter()
plotter.add_mesh(ant, 'r')
plotter.add_mesh(ant_copy, 'b')

# Add airplane mesh and make the color equal to the Y position.  Add a
# scalar bar associated with this mesh
plane_scalars = airplane.points[:, 1]
plotter.add_mesh(airplane, scalars=plane_scalars,
                 scalar_bar_args={'title': 'Airplane Y\nLocation'})

# Add annotation text
plotter.add_text('Ants and Plane Example')
plotter.show()