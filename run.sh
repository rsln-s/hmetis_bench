#!/bin/bash

# folders=( communities_hmetis_1 communities_hmetis_2 communities_hmetis_3 communities_hmetis_4 )

folders=( hmetis_SNAP1 hmetis_SNAP2 hmetis_SNAP3 hmetis_SNAP4 hmetis_SNAP5 hmetis_SNAP6 hmetis_SNAP7 hmetis_SNAP8 hmetis_SNAP9 hmetis_SNAP10 ) 

cd /home/rshaydu/hmetis_bench

for d in "${folders[@]}"
do
	cp run.py $d
	cp hmetis2.0pre1 $d
	qsub -v dir=$d for_dir.pbs
done
