# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:14:06 2021

@author: liz
"""

from bs4 import BeautifulSoup
#from lxml import etree
import os
from os import path

directory = 'staging'
outputdirectory = 'cleaned'

for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        xmlfile = path.join(directory, filename)
        with open(xmlfile, 'r') as file:
            soup = BeautifulSoup(file, "lxml-xml")           
        
        for did in soup.find_all("did"):
# make a list of all the children of did. If the list is exactly equal to 1...
# https://linuxhint.com/find_children_nodes_beautiful_soup/
            if len(list(did.findChildren("dao"))) == 1:
# then remove the daodesc
                for daodesc in soup.findChildren("daodesc"):
                    daodesc.decompose()
                        
outputpath = path.join(outputdirectory, filename)
#write to file
with open(outputpath, 'w') as outfile:
          outfile.write(str(soup))