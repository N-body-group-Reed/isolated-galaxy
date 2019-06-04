from pyICs.density_profiles import *
from pyICs.am_profiles import *
from pyICs.equilibrium_halos import *
from pyICs.tools import *
import numpy as np
from pyICs import create_ics
N=2e5 #number of particles (should match sim)
a=20*.98*N**(-.26) #calculation of a. note that N^-.26 is softening length
def rho(r, pars):
	return np.heaviside(7*a-r,.5)*((1.0+20*r/a)**(-.75))*((1.0+r/(5*a))**(-2.5))
def drhodr(r, pars):
	return np.heaviside(7*a-r,.5)*(-139.754*(r/a+5)**(-3.5)*(20*r/a+1)**(-.75)-838.525*(r/a+5)**(-2.5)*(20*r/a+1)**(-1.75))/a
def d2rhodr2(r, pars):
	return np.heaviside(7*a-r,.5)*(.35*(r/(5*a)+1)**(-4.5)*(20*r/a+1)**(-.075) +15*(r/(5*a)+1)**(-3.5)*(20*r/a+1)**(-1.75) + 515*(r/(5*a)+1)**(-2.5)*(20*r/a+1)**(-2.75))/(a**2)
pars={'a':10} 
sim = create_ics(profile = rho,drhodr=drhodr,d2rhodr2=d2rhodr2,fname = "noahgasnostars.out",m_vir='1e12 Msol', n_particles = 2e5,spin_parameter=.3)
# distribution rho and particle count ripped from p. 67 of Noah Muldavin's thesis
# not sure how to implement his velocity distribution, so didn't bother in this one
# Added cutoff from Noah's thesis, might impact normalization (implemented with heaviside theta)
