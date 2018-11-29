# Initial conditions to create simplest possible halo initial conditoins
# This will not form stars.  Only a dark matter and gas halo.
# A reference for why this code will not form stars would be helpful
# presumably the pyICs site has a clue
#
from pyICs.density_profiles import *
from pyICs.am_profiles import *
from pyICs.equilibrium_halos import *
from pyICs.tools import *

sim = EquilibriumHalo()
sim.make_halo()
sim.finalize()
