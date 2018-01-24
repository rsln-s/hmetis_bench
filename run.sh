#!/bin/bash

folders=( add20 )

imbals=( 3 5 10 )
# parts=( 2 4 8 16 32 64 128 )

for i in "${imbals[@]}"
do
        for d in "${folders[@]}"
        do
			qsub -v dir=$1,subdir=$d$i,imbal=$i for_dir.pbs
        done
done
