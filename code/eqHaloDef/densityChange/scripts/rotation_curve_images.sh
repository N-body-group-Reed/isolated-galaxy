#!/bin/bash
view="-fo"
basename=
if [[ "$1" = "-"* ]]; then
    echo Provide basename as first positional paraemter
    exit 1
else
    basename=$1
    shift
fi
if [ -z "$basename" ]; then
    echo Basename is empty.
    exit 1
fi
while [ "$1" != "" ]; do
    case $1 in
        -fo | --face_on )       view=$1
                                ;;
        -so | --side_on )       view=$1
                                ;;
        -h  | --help    )       usage
                                exit
                                ;;
        *               )       usage
                                exit 1
    esac
    shift
done
mkdir -p ../images/$basename/rotation_curves
prefix="v_${view:1}"
for file in ../$basename.*
do
    case $file in *.den)        continue;; esac
    case $file in *.Metalsdot)  continue;; esac
    case $file in *.chk*)       continue;; esac
    case $file in *.log)        continue;; esac
    case $file in *.out)        continue;; esac
    case $file in *.timings)    continue;; esac
    
    python3.7 rotation_curve_image.py -f $file $view 
    mv "$prefix"_"$basename"* ../images/$basename/rotation_curves
done
python3.7 to_gif.py $basename -p "$prefix" -m rotation_curves
