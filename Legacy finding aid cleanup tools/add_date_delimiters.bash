#!/bin/bash
#for adding ISO-compatible delimiters to dates (handy with legacy finding aids)
#to use, change 'testfile.txt' and 'testfile2.txt' to actual filename
#copy and paste into command line
path=mnt/g/'My Drive'/'Collections & Processing'/
cat $path/testfile.txt | perl -pe 's/(\d{4})(\d{2})(\d{2})/$1-$2-$3/g' | perl -pe 's/(\d{4})(\d{2})(\D)/$1-$2$3/g' > $path/testfile2.txt
