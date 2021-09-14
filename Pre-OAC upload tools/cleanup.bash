#!/bin/bash
#standard pre-OAC-ingest cleanups for finding aids exported from ArchivesSpace
path=/mnt/c/Users/ecphillips/staging
for file in $path/*.xml
do
    cat $file | sed 's|<unitid audience="internal" identifier="[0-9]\+" type="Archivists Toolkit Database::RESOURCE">[0-9]\+</unitid>||g' > $file.2
	mv $file.2 $file
	tidy -emq -config /usr/share/tidy1.cfg $file
	cp $file $file.bak
	cat $file | sed 's/Davis General Library/Davis Library/g' | sed 's/"creator"/"Creator"/g' | sed 's/latn/Latn/g' | sed 's|http://www.lib.ucdavis.edu/dept/specol/|https://www.library.ucdavis.edu/archives-and-special-collections|g' | sed 's|"0/0"|"0000"|g' | sed 's|xlink:audience="internal"||g' | sed 's|xlink:audience="external"||g' | sed 's/ns2:type="simple"//g' | sed 's|<dsc />||g' | sed 's|,</unittitle>|</unittitle>|g' | sed 's|,</unitdate>|</unitdate>|g' > $file.2
	mv $file.2 $file
done
diff -b  $path/*.bak $path/*.xml | less
