import pynbody
import argparse
import sys
import matplotlib.pylab as plt
import os
from os import environ
# load the snapshot and set to physical units

parser = argparse.ArgumentParser(description="Pass a file path to generate a gas density image.")
parser.add_argument("-f", "--file", dest="file", 
                    help = "Pass specified file to find gas temperature image.  Will display first halo unless" + 
                    "specified otherwise")
parser.add_argument("-fo", "--face_on", action="store_true",
                    help = "Visualize face-on perspective (default).")
parser.add_argument("-so", "--side_on", action="store_true", 
                    help = "Visualize the side-on perspective.")
parser.add_argument("-c", "--color", dest="color", 
                    help = "Pass color key for pynbody visualization.  Default is \"Greys\"")

args = parser.parse_args()
face_flag = True
if args.face_on and args.side_on:
    print("Pass only one of --side_on or --face_on")
    sys.exit()
elif args.side_on:
    face_flag = False
else:
    pass
snap = pynbody.load(args.file)

if face_flag:
    pynbody.analysis.angmom.faceon(snap)
    flag_str = "fo"
else:
    pynbody.analysis.angmom.sideon(snap)
    flag_str = "so"
# create a profile object for the stars
snap.physical_units()
p = pynbody.analysis.profile.Profile(snap,min=.01,max=250,type='log',ndim=3)
pg = pynbody.analysis.profile.Profile(snap.g,min=.01,max=250,type='log',ndim=3)
ps = pynbody.analysis.profile.Profile(snap.s,min=.01,max=250,type='log',ndim=3)
pd = pynbody.analysis.profile.Profile(snap.d,min=.01,max=250,type='log',ndim=3)

# make the plot
plt.plot(p['rbins'],p['v_circ'],label='total')
plt.plot(pg['rbins'],pg['v_circ'],label='gas')
plt.plot(ps['rbins'],ps['v_circ'],label='stars')
plt.plot(pd['rbins'],pd['v_circ'],label='dm')

name=os.path.basename(args.file)
name = name.replace(".", "_")

plt.xlabel('R [kpc]')
plt.ylabel(r'$v_c$ [km/s]')
plt.legend()
plt.title(name)
plt.savefig("v_"+flag_str+"_"+name)