import imageio
import argparse
from os import walk

parser = argparse.ArgumentParser(description="Creates a gif from all images with a specific basename.")
parser.add_argument("basename",
                    help="Specify the simulation basename to run on.")
parser.add_argument("-s", "--suffix", dest="suffix", 
                    help="Specify a suffix to append to the gif name.")
parser.add_argument("-p", "--prefix", dest="prefix",
                    help="Specify a prefix to append to the gif name.")
args = parser.parse_args()

prefix = args.prefix
suffix = args.suffix
basename = args.basename
if prefix != None:
    basename = prefix + "_" + basename
if suffix != None:
    basename += suffix

with imageio.get_writer("../images/"+args.basename+"/"+basename+".gif", 
                        mode='I', duration=0.3) as writer:
    print("here")
    filenames = []
    for (dirpath, dirnames, fnames) in walk("../images/"+args.basename):
        filenames.extend(fnames)
        break
    for filename in filenames:
        image = imageio.imread("../images/"+args.basename+"/"+filename)
        writer.append_data(image)
