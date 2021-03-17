#!/bin/bash
#pre-MARCEdit XSLT cleanups for finding aids
path=/mnt/c/Users/ecphillips/ead_for_marc
for file in $path/*.xml
do
    tidy -emq -config /usr/share/tidy1.cfg $file
    cp $file $file.bak
    cat $file | sed 's|xmlns="urn:isbn:1-931666-22-9"||g' | sed 's/xlink://g' | sed 's/linear feet//g' | sed 's|<head>Preferred Citation</head>||g' | sed 's|<head>History</head>||g' | sed 's|<head>Biography</head>||g'  | sed 's|<head>Scope and Contents</head>||g' | sed 's|.</p>|. </p>|g' | sed 's|<head>Biographical / Historical</head>||g' > $file.2
    mv $file.2 $file
done
diff -b  $path/*.bak $path/*.xml | less
