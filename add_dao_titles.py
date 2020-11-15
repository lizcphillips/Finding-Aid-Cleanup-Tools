# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:11:33 2020

@author: ecphillips
"""
#Add title element to <dao> based on <unittitle>

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
    #counter - is the loop iterating right?
    i = 0
    for elem in tree.xpath('.//c01/c02'):
        print(i)
        unittitle = (elem.findtext('.//did/unittitle'))
        dao = (elem.find('.//did/dao'))
        #basic error handling
        if dao is None:
            continue
        dao.attrib['title'] = unittitle
        i = i+1
#print to stdout to double-check
print(etree.tostring(root, encoding='utf-8').decode('utf-8'))
outputpath = path.join(outputdirectory, filename)
#write to file
with open(outputpath, 'w') as outfile:
           outfile.write(etree.tostring(root, encoding='utf-8').decode('utf-8'))
