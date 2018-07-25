# **Description**
These programs are meant to test default characteristics of the equilibrium class in pyICs.  Each one singles out a few specific characteristics in the constructor to test how they affect the the created halos.
# **Programs**
## default
The result of running the default constructor.  The default constructor calls the *alpha-beta-gamma* density function and its derivatives.  The virial mass is 1e12 MSol.  The default number of particles are 1e5.
## particleIncrease
Increases the total particle count by a factor of 100 using the `n_particles` parameter.  Additionally, the file name is modified with the `fname` parameter in the constructor.
## densityChange
Changing the alpha-beta-gamma parameters to random values.  Meant to test the specific effects on the simulation.  Compared against the result of **default**
