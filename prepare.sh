#!/bin/bash
if [ "$#" -ne 1 ]; then
	echo "You have to pass a directory name to this script"
	exit 0
fi

folders=( add20 )

imbals=( 3 5 10 )
# parts=( 2 4 8 16 32 64 128 )

mkdir /scratch2/rshaydu/bench_trilinos_zoltan/$1
mkdir /home/rshaydu/bench_trilinos_zoltan/$1

for i in "${imbals[@]}"
do
	for d in "${folders[@]}"
	do
		# prepare directory 
		mkdir /scratch2/rshaydu/bench_trilinos_zoltan/$1/$d$i
		cd /scratch2/rshaydu/bench_trilinos_zoltan/$1/$d$i

		cp /home/rshaydu/hypergraphs_hmetis/"$d".mtx.hmetis .
		cp /home/rshaydu/hmetis_bench/run.py .
		cp /home/rshaydu/hmetis_bench/hmetis2.0pre1 .
	done
done
