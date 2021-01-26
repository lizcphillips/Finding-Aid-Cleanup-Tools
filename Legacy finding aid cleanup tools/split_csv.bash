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
    echo $data | split -l 1000 $file $file.2
    #$file.2* (* part) is a glob - this will go through all of the files
    #tempfile gives the for loop something to grab & work with
    #this counter makes it possible to treat the first split differently
    (( i=0 ))
    for tempfile in $file.2*
    do
	#check to see if this is the first split - if it is, don't add the header (it's already there)
	if (( i > 0 ))
	then
	    #pass header back to parts
	    #sed statement within quotes: 1i is its own command (see man page)
	    sed -i "1i$header" $tempfile
	fi
        #rename file to .csv
	mv $tempfile $tempfile.csv
	(( i=i +1 ))
    done
done
