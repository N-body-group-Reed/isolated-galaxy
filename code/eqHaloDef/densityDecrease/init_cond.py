# Use alpha beta gamma parameters to change the density 
# Compare the density to the default one with the same number of particles

# Parameter descriptions:
# pars: Dictionary with profile parameters which must contain the following:
#         alpha: Parameter that controls width of the transition between inner and
#             outer slope
#         beta: Outer slope
#         gamma: Inner slope
#         c (only necessarry if b <= 3): Concentration parameter (R_vir/R_s)
#         factor (only necessarry if b <= 3): Scale length for exponential cutoff
#            in units of R_vir


# Dark matter halo default parameters -- alpha = 1, beta = 3, gamma = 1
# Equilibrium halo default parameters -- alpha = 1, beta = 3, gamma = 1

from pyICs.density_profiles import *
from pyICs.am_profiles import *
from pyICs.equilibrium_halos import *
from pyICs.tools import *
params = {'alpha': 5, 'beta': 2, 'gamma': 1, 'c': 10, 'factor': 0.1}

sim = EquilibriumHalo(pars=params, fname = "halo.tbin", n_particles = 1e6)
sim.make_halo()
sim.finalize();
