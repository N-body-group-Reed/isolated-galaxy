import imageio
import argparse
from os import walk

parser = argparse.ArgumentParser(description="Creates a gif from all images with a specific basename.")
parser.add_argument("basename",
                    help="Specify the simulation basename to run on.")
parser.add_argument("-m", "--my_path", dest="path", 
                    help="Specify the path in images to save the gif, e.g., \"gas_density\".  Default is blank.")
parser.add_argument("-s", "--suffix", dest="suffix", 
                    help="Specify a suffix to append to the gif name.")
parser.add_argument("-p", "--prefix", dest="prefix",
                    help="Specify a prefix to append to the gif name.")
args = parser.parse_args()

prefix = args.prefix
suffix = args.suffix
path = args.path
basename = args.basename
if prefix != None:
    basename = prefix + "_" + basename
if suffix != None:
    basename += suffix
if path == None:
    path = ""
path = path.replace(" ", "")
with imageio.get_writer("../images/"+args.basename+"/"+path+"/"+basename+".gif", 
                        mode='I', duration=0.3) as writer:
    filenames = []
    for (dirpath, dirnames, fnames) in walk("../images/"+args.basename+"/"+path):
        filenames.extend(fnames)
        break
    for filename in filenames:
        if basename in filename:
            image = imageio.imread("../images/"+args.basename+"/"+path+"/"+filename)
            writer.append_data(image)
