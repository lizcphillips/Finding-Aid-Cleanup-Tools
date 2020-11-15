# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:22:47 2020

@author: ecphillips
"""
#Remove Archivists Toolkit unitids from legacy finding aids

from lxml import etree
import os
from os import path

directory = 'staging'
outputdirectory = 'cleaned'

for filename in os.listdir(directory):
    if filename.endswith(".xml"):
       xmlfile = path.join(directory, filename)
       #with statement takes care of closing file at end
       with open(xmlfile, 'r', encoding = 'utf-8') as f:
           #read file and hold in memory
           content = f.read()
           tree = etree.parse(xmlfile)
           root = tree.getroot()
       i = 0
       #https://riptutorial.com/xpath/example/10546/find-nodes-by-substring-matching-of-an-attribute-s-value
       #print(elem)
       for elem in tree.xpath(".//*[contains(@type, 'Archivists Toolkit Database')]"):
           print(i)
           elem.getparent().remove(elem)               
           i = i+1
#take file in memory and put it somewhere...
print(etree.tostring(root, encoding='utf-8').decode('utf-8'))
#direct the output to separate directory
outputpath = path.join(outputdirectory, filename)
#the actual writing/closing part
with open(outputpath, 'w') as outfile:
    outfile.write(etree.tostring(root, encoding='utf-8').decode('utf-8'))
