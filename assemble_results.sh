#!/bin/bash
if [ "$#" -ne 1 ]; then
	echo "You have to pass a directory name to this script"
	exit 0
fi

mkdir "$1"_res

folders=( blah1 blah2 )

for d in "${folders[@]}"
do
	if [ -f $d/output.csv ]; then
		cp $d/output.csv "$1"_res/
		mv "$1"_res/output.csv "$1"_res/output_"$d".csv
	fi
done

cat "$1"_res/*.csv > "$1"_res/"$1"_merged.csv
