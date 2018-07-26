echo Enter the simulation basename.
read basename

mkdir -p ../images/$basename

for file in ../$basename.*
do
    case $file in *.den)        continue;; esac
    case $file in *.Metalsdot)  continue;; esac
    case $file in *.chk*)       continue;; esac
    case $file in *.log)        continue;; esac
    case $file in *.out)        continue;; esac
    case $file in *.timings)    continue;; esac
    
    python3.7 gas_density_image.py -f $file
    mv *$basename* ../images/$basename 
done