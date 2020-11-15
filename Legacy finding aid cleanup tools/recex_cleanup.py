# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:01:40 2020

@author: ecphillips

"""
#Clean up collection-level records exported from RecordExpress prior to ingesting into ArchivesSpace

from lxml import etree
import os
from os import path

directory = 'recexstaging'
outputdirectory = 'recexcleaned'

for filename in os.listdir(directory):
    if filename.endswith(".xml"):
       xmlfile = path.join(directory, filename)
       tree = etree.parse(xmlfile)
       root = tree.getroot()
       #https://stackoverflow.com/a/6524105
	   #replace <author>
       tree.find('.//author').text = 'Finding aid created by Archives and Special Collections staff'
       title = (root.findtext('./eadheader/filedesc/titlestmt/titleproper'))
       callno = (root.findtext('./eadheader/eadid'))
       #https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
       #reformat <prefcite> note
       tree.find('./archdesc/prefercite/p').text = ('[Identification of item], {0:s}, {1:s}, Archives and Special Collections, UC Davis Library, University of California, Davis.'.format(title, callno))
       #remove empty <acqinfo> note
       for elem in tree.xpath('//acqinfo'):
           elem.getparent().remove(elem)
		   #remove subject headings to avoid duplication in ArchivesSpace tables
           for elem in tree.xpath('//controlaccess'):
               elem.getparent().remove(elem)
		   #remove link to PDF list
           for elem in tree.xpath('//otherfindaid'):
               elem.getparent().remove(elem)      
       #print reformatted XML to verify output
       print(etree.tostring(root, encoding='utf-8').decode('utf-8'))
       #save the reformatted XML to the output directory
       outputpath = path.join(outputdirectory, filename)
       with open(outputpath, 'w') as outfile:
           outfile.write(etree.tostring(root, encoding='utf-8').decode('utf-8'))
