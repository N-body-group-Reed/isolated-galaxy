import pynbody
import numpy as np
import array
import math

import pynbody.plot.sph as sph

import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

def traceThing(path, index, interval, nsteps): 
    #tracing function
    #How this works: out files are in form [path]/[name].000005
    #path is a string: give it '[path]/[name]'. Note that path is wrt current folder.
    #for example, if in the same folder as target outputs, just give this function [name]
    #index should be an integer: its how we pull a specific particle out of the pynbody file.
    #interval is the step difference between outputs: give it an integer corresponding to that (i.e. 5)
    #nsteps should be less than or equal to the total number of steps in the simulation. 
    #Would expect an integer, but takes any kind of number.
    #this function returns the location of the given particle at each output file.
    part=[]
    t=interval
    while (t <= nsteps):
        s=pynbody.load(path+'.'+str(t).zfill(6))
        s.physical_units()
        part.append([s.dm['x'][index],s.dm['y'][index],s.dm['z'][index]])
        t+=interval
    return part #should be array of 3tuples.

def radialIndexFinder(path,rmin,rmax):
    #produces list of indices of particles that are between radii rmin and rmax.
    #helper function for spiralFinder.
    i=0
    l=[] #empty list
    s=pynbody.load(path)
    s.physical_units()
    k=s.dm['pos']
    for p in k:
        if(rmin<=np.linalg.norm(p)<=rmax):
            l.append(i)
        i+=1
    return l

def maxDensity(path, ring, nSec): #returns indices of particles in ring.
    #helper function for spiralFinder
    i=0.0
    theta=2*math.pi/nSec
    s=pynbody.load(path)
    ray= [[]]*nSec #create list of nSec empty lists. This way makes it so that initializ
    x=0
    for x in range(nSec): #cycles through each each empty list.
        for l in ring: #adds indices of particles in a specific sector into corresponding array space.
            if i<= np.arctan2(s.gas['x'][l],s.gas['y'][l]) <i+theta:
                ray[x].append(l)
        i+=theta
    x=0 #keeps track of current index
    xm=0 #keeps track of index of longest list
    z=len(ray[0]) #z is value of longest list
    for k in ray: #goes through newly filled lists, and picks the longest one.
        if len(k) > z:
            z=len(k)
            xm=x
        x+=1
    return ray[xm] #returns the angle sector and the longest list of indices.
#considering changing to just longest list of indices to match.
#Implemented the above change.

def spiralFinder(path,rmin,rmax,nSec):
    #finds highest density slice in an area. Hopefully should pick out spiral arms. likely error prone.
    #Someone vulnerable to thresholds due to particle drift.
    k=radialIndexFinder(path,rmin,rmax)
    return maxDensity(path,k,nSec)[1] #returns list of indices 

def sectorFinder(s,xmin,xmax,ymin,ymax): 
    #picks out particles in a given square. potentially change this to respect 3space.
    s
    k=s.dm['pos']
    l=[]
    i=0 #index tracker
    for p in k:
        if (xmin<=p[0]<xmax and ymin<=p[1]<ymax):
            l.append(i)
        i+=1
    return l

#
# Example usage
#
part=traceThing('writeTest/btStars/btStars',20,5,1000)

x=[[]]*len(part)
y=[[]]*len(part)
z=[[]]*len(part)
for n in range(len(part)):
    x[n]=part[n][0]
    y[n]=part[n][1]
    z[n]=part[n][2]
fig =plt.figure()
ax=fig.add_subplot(111,projection='3d')

ax.scatter(x,y,z,c='r', marker='o')
plt.show()
