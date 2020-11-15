# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5 10:47:00 2020

@author: ecphillips
"""
#Remove redundant <daodesc>
#Note: if this is failing, try deleting xmlns="urn:isbn:1-931666-22-9" from
#the root tag. Remember to put it back before trying to upload.

from lxml import etree
import os
from os import path

directory = 'staging'
outputdirectory = 'cleaned'

for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        xmlfile = path.join(directory, filename)
        tree = etree.parse(xmlfile)
        root = tree.getroot()

        i = 0
        for elem in tree.xpath('.//daodesc'):
            print(i)
            elem.getparent().remove(elem)
            i = i+1
   
outputpath = path.join(outputdirectory, filename)
with open(outputpath, 'w') as outfile:
           outfile.write(etree.tostring(root, encoding='utf-8').decode('utf-8'))
