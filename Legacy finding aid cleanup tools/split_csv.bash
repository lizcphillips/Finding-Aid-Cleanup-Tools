#!bin/bash
#split a CSV file into 500 line increments while keeping the headers - good for AS ingest CSVs
path=/mnt/c/Users/ecphillips/box_lists
for file in $path/*.csv
do
    #split off header
    header=$(head -1 $file)
    #define tail
    data=$(tail -n +2 $file)
    #split up file
    echo $data | split -l 2000 $file $file.2
    #$file.2* (* part) is a glob - this will go through all of the files
    #tempfile gives the for loop something to grab & work with
    for tempfile in $file.2*
    do
	#pass header back to parts
	#sed statement within quotes: 1i is its own command (see man page)
	sed -i "1i$header" $tempfile
	#rename file to .csv
	mv $tempfile $tempfile.csv
    done
done
