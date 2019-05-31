from pyICs.density_profiles import *
from pyICs.am_profiles import *
from pyICs.equilibrium_halos import *
from pyICs.tools import *
from pyICs import create_ics

def rho(r, pars):
	return ((1.0+r/.075)**(-.75))*((1.0+r/.375)**(-2.5))
def drhodr(r, pars):
	return -6.66667*(2.66667*r+1)**(-3.5)*(13.3333*r+1)**(-.75)-10*(2.66667*r+1)**(-2.5)*(13.3333*r+1)**(-1.75)
def d2rhodr2(r, pars):
	return 62.2222*(2.66667*r+1)**(-4.5)*(13.3333*r+1)**(-.075) +133.333*(2.66667*r+1)**(-3.5)*(13.3333*r+1)**(-1.75) + 233.333*(2.66667*r+1)**(-2.5)*(13.3333*r+1)**(-2.75)
pars={'sig':10}
sim = create_ics(profile = rho,drhodr=drhodr,d2rhodr2=d2rhodr2,fname = "noahgasnostars.out",m_vir='1e12 Msol', n_particles = 2e5,spin_parameter=.3)
# distribution rho and particle count ripped from p. 67 of Noah Muldavin's thesis
# not sure how to implement his velocity distribution, so didn't bother in this one
#sim.make_halo()
#sim.finalize()
