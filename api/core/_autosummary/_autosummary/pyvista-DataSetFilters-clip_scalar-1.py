# Remove the part of the mesh with "sample_point_scalars" above 100.
#
import pyvista as pv
from pyvista import examples
dataset = examples.load_hexbeam()
clipped = dataset.clip_scalar(scalars="sample_point_scalars", value=100)
clipped.plot()
#
# Remove the part of the mesh with "sample_point_scalars" below
# 100.  Since these scalars are already active, there's no need
# to specify ``scalars=``
#
import pyvista as pv
from pyvista import examples
dataset = examples.load_hexbeam()
clipped = dataset.clip_scalar(value=100, invert=False)
clipped.plot()
