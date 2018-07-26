#Generate gas density profiles from file name passed as 
#command line argument.  Saves image in images/gas_density/

#command line options: -f = faceon view
#                      -s = sideon view
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt
import argparse
import sys
import os

parser = argparse.ArgumentParser(description="Pass a file path to generate a gas density image.")
parser.add_argument("-f", "--file", dest="file", 
                    help = "Pass specified file to find gas density image.  Will display first halo unless" + 
                    "specified otherwise")
parser.add_argument("-fo", "--face_on", action="store_true",
                    help = "Visualize face-on perspective (default).")
parser.add_argument("-so", "--side_on", action="store_true", 
                    help = "Visualize the side-on perspective.")
parser.add_argument("-c", "--color", dest="color", 
                    help = "Pass color key for pynbody visualization.  Default is \"Greys\"")
parser.add_argument("-w", "--width", dest="width", type=int, 
                    help = "Width used in analysis.  Default is 100.")

args=parser.parse_args()
face_flag = True
if args.face_on and args.side_on:
    print("Pass only one of --side_on or --face_on")
    sys.exit()
elif args.side_on:
    face_flag = False
else:
    pass
snap = pynbody.load(args.file)
snapTime = pynbody.load(args.file)
snap.physical_units()
snapTime.physical_units('Gyr')
viewStr = ""

if face_flag:
    print(pynbody.analysis.angmom.faceon(snap))
    viewStr="fo"
else:
    print(pynbody.analysis.angmom.sideon(snap))
    viewStr="so"

if args.width is None: 
    width=100 
else: 
    width=args.width

if args.color is None: 
    cmap = "Greys" 
else: 
    cmap = args.color

name=os.path.basename(args.file)
name = name.replace(".", "_")
pynbody.plot.image(snap.g, qty = "rho", units = "g cm^-3", width=width, cmap=cmap, filename="gd_"+viewStr+"_"+cmap+"_"+os.path.basename(name), 
                    title=snapTime.properties['time'])
