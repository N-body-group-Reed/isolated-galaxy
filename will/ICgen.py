import numpy as np
from pynbody import array, new, snapshot, units
from pynbody import gadget, grafic, nchilada, ramses, tipsy
import pynbody as pyn
import math
import scipy
import scipy.special as scp
#I think these two are only useful for plotting.
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#
# Generates a list of three different lists, in order: [x,y,z] position, [x,y,z] velocity, and radius.
# Overall goal is to generate particles that roughly correspond to a specific density distribution.
#
def genPartList(rmax,ntot,nbins,denFunc,rotafunc): 
    #assumes radial symmetry on function. Produces list of particles locations.
    #Should be roughly axisymmetric.
    n=0.0 
    starList=[]
    velList=[]
    rList=[]
    dr = rmax/nbins #nbins is the "specificity" of the distribution, ntot is the average number of particles, rmax is the cutoff radius of the disk.
    for n in range(0,ntot):
        r=0.0 
        while r < rmax: #important to note that rmax is a hard cutoff.
            if(np.random.random() < denFunc(r+dr/2)*r*dr*2*math.pi):
                #finds probability that there is a particle in the given slice(0<p<1) and rolls between 0 and 1.
                #if that number is below the probability, a particle is randomly placed in the slice.
                #Note that this assumes the integral of the density function is normalized to 1.
                rt=r+np.random.random()*dr
                disp=vDisp(rt)
                vt=rotafunc(rt,disp)#calculates tangential velocity including dispersion.
                vrad=vr(rt,disp)#calculates radial velocity including dispersion.
                thetem=np.random.random()*2*math.pi
                x=rt*math.cos(thetem)
                vx=(math.sin(thetem)*vt+math.cos(thetem)*vrad) #changing it to work like this should reduce number of calls
                #velocity is currently decided based onwhatever the seeding function
                y=rt*math.sin(thetem)
                vy=(-math.cos(thetem)*vt+math.sin(thetem)*vrad)
                z=np.random.normal(0,.105) #sort of a placeholder: will add distribution option eventually.
                vz=0#np.random.normal(0,3*vdisp)*.5 #3*vdisp is from initialize.cpp.
                starList.append([x,y,z])
                velList.append([vx,vy,vz])
                rList.append(rt)
            r+=dr
    return [starList,velList,rList]
#
# Some "helper" functions to feed into genPartList. Normalized surface density.
#
def noahDenFunc(r):
    return ((1+20*r*1/1.5)**(-.75)*(1+r*1/7.5)**(-2.5)/3.96716)
def dmHaloFunc(r):
    return ((1/((1+r/10.0)**3))/250.87)
def expDist(r):
    return math.exp(-r)
#
# Rotation functions
#
def vt(r,disp):#ripped out of sellwood paper, implementation of velocity dispersion.
    return np.random.normal(r/1.5*(1+2*r/1.5)**(-.875)*(1+r/7.5)**(-.625),disp) 
def vtSimp(r,disp): #version of vt simply geared toward stability, assuming simple circular orbits.
    #take r in kpc, disp in m/s. Apparently this hasn't fixed the explosion problem.
    pot=simpson(dForce,r,0,100) #in kilograms
    v=np.sqrt(pot*2/m)
    return np.random.normal(v,disp)#moving to km/s at the end.
#
# Radial Dispersion
#
def vr(r,disp): #functionally just a repackaging of np.random.normal. Will probably remove for efficiency.
    return np.random.normal(0,disp)
#
# Converts tangential velocity to x-y velocity. Treats clockwise as positive direction.
# Probably both have been obseleted, because I realized that I can just plug in rotafunc.
#
def veltX(r,theta, rotafunc,disp):
    return math.sin(theta)*rotafunc(r,disp)
def veltY(r,theta, rotafunc,disp):
    return -math.cos(theta)*rotafunc(r,disp)# I think the - sign might fix things, we'll see.
#
# Converts radial velocity to x-y velocity. Similarly obselete.
#
def velrX(r,theta, rotafunc,disp):
    return math.cos(theta)*rotafunc(r,disp)
def velrY(r,theta, rotafunc,disp):
    return math.sin(theta)*rotafunc(r,disp)

#
# Standard simpson integral. Not much to say about this.
#
def simpson(f, xn,x0,n):
    x=f(x0)+f(xn)
    dx=(xn-x0)/n
    for k in range(1,n,2): #switched to for k in range to cut down on line mileage
        x+=4*f(x0+k*dx)
    for k in range(2,n-1,2):
        x+=2*f(x0+k*dx)
    return x*dx/3
#
# Calculator for initial potential. uses simpson integral.
#
G= 4.30091E-6 #kpc/Msol*(km/s)^2.
# These specific units were on wikipedia. Astrophysics is wierd.
#
m=1000 #Msol -> manually adjust to match particle masses. Will incorporate into full genPartList func eventually.
#
def calcPhi(f, r, nbin): #Calculates potential based on distribution function.
    #I think this function is fundamentally broken: first, the disk may not be uniform enough to cleanly integrate.
    #additionally, this functio ndoes not compensate for changes in enclosed mass as a particle moves towards the center of a well. Also the calculation is wrong because shells don't exist.
    return simpson(f,r,0,nbin)*G*m/r

#
# Page 99, eq. 2.157 of Binney and Tremaine. Big hope for this one.
# Generalization of this function so far isn't working.
#
def btVel(r,a,dfunc):
    def aInt(aQ):
        return aQ/np.sqrt(r**2-aQ**2)
    def aDer(ap):
        def rpInt(rp):
            return rp*dfunc(rp)/np.sqrt(rp**2-ap**2)
        return simpson(rpInt,10*a,ap,100) #this is written as an infinite integral, but i'm hoping 10 a is apprx. large enough.
    return -4*G*simpson(aInt,r-.001,0,100)*scipy.misc.derivative(aDer,a)
#
# specific case for exponential disk.
#
def expDistVel(r,disp):
    vSqr=4*math.pi*G*(m*20000)*(r/2)**2*(scp.iv(0,r/2)*scp.kn(0,r/2)-scp.iv(1,r/2)*scp.kn(1,r/2))
    return np.random.normal(np.sqrt(vSqr),disp)
#
# Some specific potential functions. collapses into single function for sake of easy integration.
# Units are mSol/kpc: integrate over a section to get the mass of that section.
# These are not useful in the way I thought they would be: shell approx does not hold for disk.
#     Keeping them around for record-keeping, but probably obselete at this point.
#
def starpot(r):
    return noahDenFunc(r)*2*math.pi*r*np.heaviside(10.5-r,1)*1.0E+11
def dmpot(r):
    return dmHaloFunc(r)*2*math.pi*r*.9E+12
def dForce(r):
    return G*m*dmpot(r)/(r**2+.075**2) #adding softening length, hopefully won't skrew up too much.
#
# Defining velocity dispersion as function of radius.
# Within scope of noah's thesis, radial and azimuthal velocity dispersions are the same. 
# See page 46 of Noah's Thesis for more details.
#
def vDisp(r): #calculates velocity dispersion according to Noah's thesis.
    Q=1.2 #Supposed to be Toomre Q parameter. Will add ability to pass in Q values.
    sigmar = noahDenFunc(r)
    k=np.sqrt(r*dOmSqdr(r)+4*OmSq(r))
    #This value needs to come out in km/s
    return 3.36*sigmar*Q/k #Using same value for radial and tangential v dispersion.
#
# helper functions for vDisp
# These are the frequencies at which particles at perfectly circular orbits would rotate. Not sure if I have to incorporate dm distribution also.
# Pretty rudimentary calculation of potential. Might exclude this from a better version.
# Need to be readjusted given that shell theorem doesn't hold.
#
def OmSq(r): #takes kiloparsecs 
    #GO THROUGH ALL OF THIS VERY CAREFULLY V-> UNITS ARE SCARY
    #lets just recalculate our value for G.
    return (G*simpson(starpot,r,0,100))/(r)**3#simpson calculation here represents value of mass
def dOmSqdr(r):
    m= simpson(starpot,r,0,100) #derivative of omega squared I think? thesis is not entirely clear about this
    return G*(starpot(r)/r**3-3*m/r**4)

#
# How these functions should be used in the end
#
starList = genPartList(10.5,2000,1000,expDist,expDistVel)
dmList = genPartList(84.0,18000,1000,expDist,expDistVel)
#
#
noahSim = pyn.new(star=len(starList[0]),dm=len(dmList[0]))#,dm=len(dmList[0]))
#
noahSim['pos'].units= 'kpc' #maybe there's something off with the units?
noahSim['vel'].units= 'km s^-1'
noahSim['mass'].units= 'Msol'
#
sl2=np.asarray(starList[2])#translating from one file format to another: functions will take np arrays, but not lists
dl2=np.asarray(starList[2])# 
#
# Setting position, velocity, softening length, mass, and potential for stars
#
noahSim.star['pos']=starList[0]
noahSim.star['vel']=starList[1]
noahSim.star['eps']=.075
noahSim.star['mass']=m
#noahSim.star['phi']=(calcPhi(starpot,sl2,1000)*len(sl2)+calcPhi(dmpot,sl2,84)*len(dl2))
#Commenting out potential until I figure out what its units should look like.
# Same as above, but for dark matter
#
noahSim.dm['pos']=dmList[0]
noahSim.dm['vel']=dmList[1]
noahSim.dm['eps']=.075
noahSim.dm['mass']=m
#noahSim.dm['phi']=(calcPhi(starpot,dl2,1000)*len(sl2)+calcPhi(dmpot,dl2,84)*len(dl2))
#
# Lazy shortcut way of doing gas. Not yet complete enough to add into the sim.
#
#noahSim.gas['x']=noahSim.star['y']
#noahSim.gas['vx']=noahSim.star['vy']
#noahSim.gas['y']=-noahSim.star['x']
#noahSim.gas['vy']=-noahSim.star['vx']
#noahSim.gas['eps']=.075
#noahSim.gas['mass']=5000000
#noahSim.gas['phi']=(calcPhi(starpot,sl2,1000)*len(sl2)+calcPhi(dmpot,sl2,84)*len(dl2))/10
#
#
noahSim['a']=1.5 #not wure what this is for
#
# Setting units and outputting .out into curent folder.
#
noahSim.write(tipsy.TipsySnap,'btStars.out')
