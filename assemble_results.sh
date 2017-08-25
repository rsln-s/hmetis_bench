#!/bin/bash
if [ "$#" -ne 1 ]; then
	echo "You have to pass a directory name to this script"
	exit 0
fi

mkdir "$1"_res

# folders=( youtube flickr release-flickr-links_x0_10 release-flickr-links_x0_200 release-flickr-links_x0_50 release-youtube-links_x0_100 release-youtube-links_x0_25 release-flickr-links_x0_100 release-flickr-links_x0_25 release-youtube-links_x0_10 release-youtube-links_x0_200 release-youtube-links_x0_50 )

folders=( amazon0302 as-735 ca-CondMat cit-HepPh email-EuAll p2p-Gnutella05 p2p-Gnutella24 roadNet-CA soc-LiveJournal1 soc-sign-Slashdot090221 web-Google wiki-Vote amazon0312 as-caida ca-GrQc cit-HepTh Oregon-1 p2p-Gnutella06 p2p-Gnutella25 roadNet-PA soc-sign-epinions soc-Slashdot0811 web-NotreDame amazon0505 as-Skitter ca-HepPh cit-Patents Oregon-2 p2p-Gnutella08 p2p-Gnutella30 roadNet-TX soc-sign-Slashdot081106 soc-Slashdot0902 web-Stanford amazon0601 ca-AstroPh ca-HepTh email-Enron p2p-Gnutella04 p2p-Gnutella09 p2p-Gnutella31 soc-Epinions1 soc-sign-Slashdot090216 web-BerkStan wiki-Talk )

for d in "${folders[@]}"
do
	if [ -f $d/output.csv ]; then
		cp $d/output.csv "$1"_res/
		mv "$1"_res/output.csv "$1"_res/output_"$d".csv
	fi
done

cat "$1"_res/*.csv > "$1"_res/"$1"_merged.csv
