#!/bin/bash
view="-fo"
color="-c Greys"
width="-w 100"
basename=
if [[ "$1" = "-"* ]]; then
    echo Provide basename as first positional paraemter
    exit 1
else
    basename=$1
    shift
fi
while [ "$1" != "" ]; do
    case $1 in
        -fo | --face_on )       view=$1
                                ;;
        -so | --side_on )       view=$1
                                ;;
        -c  | --color   )       shift
                                color="-c $1"
                                ;;
        -w  | --width   )       shift
                                width="-w $1"
                                ;;
        -h  | --help    )       usage
                                exit
                                ;;
        *               )       usage
                                exit 1
    esac
    shift
done
mkdir -p ../images/$basename
for file in ../$basename.*
do
    case $file in *.den)        continue;; esac
    case $file in *.Metalsdot)  continue;; esac
    case $file in *.chk*)       continue;; esac
    case $file in *.log)        continue;; esac
    case $file in *.out)        continue;; esac
    case $file in *.timings)    continue;; esac
    
    python3.7 gas_density_image.py -f $file $view $color $width
    mv *$basename* ../images/$basename
done
