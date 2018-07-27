# Slightly more advanced initial conditions.
# Goal is to correct last eqHaloDef test and create stars by increasing the particle count 
# and hopefully the density
from pyICs.density_profiles import *
from pyICs.am_profiles import *
from pyICs.equilibrium_halos import *
from pyICs.tools import *

parsNFW    = {'alpha': 1, 'beta': 3, 'gamma': 1, 'c': 20}
parsHrn    = {'alpha': 1, 'beta': 4, 'gamma': 1, 'c': 1}
parsJff    = {'alpha': 1, 'beta': 4, 'gamma': 2, 'c': 1}
parsArb    = {'alpha': 1.4, 'beta': 4, 'gamma': 2, 'c': 1}
simNFW = EquilibriumHalo(fname = "haloNFW.out", n_particles = 1e7, pars=parsNFW)
simHrn = EquilibriumHalo(fname = "haloHrn.out", n_particles = 1e7, pars=parsHrn)
simJff = EquilibriumHalo(fname = "haloJff.out", n_particles = 1e7, pars=parsHrn)
simArb = EquilibriumHalo(fname = "haloArb.out", n_particles = 1e7, pars=parsArb)

simNFW.make_halo()
simHrn.make_halo()
simJff.make_halo()
simArb.make_halo()

simNFW.finalize()
simHrn.finalize()
simJff.finalize()
simArb.finalize()