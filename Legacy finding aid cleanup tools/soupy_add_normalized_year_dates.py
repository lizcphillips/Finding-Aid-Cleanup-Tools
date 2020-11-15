# -*- coding: utf-8 -*-
"""
Created on Fri Nov 06 2020

@author: ecphillips
"""
# Add missing normal dates (currently only works right for year dates - this
# passes in expression date verbatim)

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
            
# https://stackoverflow.com/questions/63744550/beautifulsoup-xml-parsing-only-return-first-result            
        for soup.unitdate in soup.find_all("unitdate"):
            date = soup.unitdate.string
            #https://stackoverflow.com/questions/10115396/
            #how-to-test-if-an-attribute-exists-in-some-xml#10115420        
            if 'normal' in soup.unitdate.attrs:
                continue
            soup.unitdate.attrs['normal'] = date
        
#print to stdout to double-check
print(soup.prettify)
outputpath = path.join(outputdirectory, filename)
#write to file
with open(outputpath, 'w') as outfile:
          outfile.write(str(soup))
