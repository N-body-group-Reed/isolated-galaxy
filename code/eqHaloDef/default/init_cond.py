# Initial conditions to create simplest possible halo initial conditoins
# This will not form stars.  Only a dark matter and gas halo
from pyICs.density_profiles import *
from pyICs.am_profiles import *
from pyICs.equilibrium_halos import *
from pyICs.tools import *

sim = EquilibriumHalo()
sim.make_halo()
sim.finalize()