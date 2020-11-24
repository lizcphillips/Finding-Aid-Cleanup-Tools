# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:28:25 2020

@author: ecphillips
"""
#linkify extref tag with https:// string

from bs4 import BeautifulSoup
import os
from os import path

directory = 'staging'
outputdirectory = 'cleaned'

for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        xmlfile = path.join(directory, filename)
        with open(xmlfile, 'r') as file:
            soup = BeautifulSoup(file, "lxml-xml")

# pass the date to the attribute            
# https://stackoverflow.com/questions/63744550/beautifulsoup-xml-parsing-only-return-first-result            
        for soup.extref in soup.find_all("extref"):
#            print(i)
            link = soup.extref.string
            #https://stackoverflow.com/questions/10115396/
            #how-to-test-if-an-attribute-exists-in-some-xml#10115420        
            if 'xlink:href' in soup.extref.attrs:
                continue      
            soup.extref.attrs['xlink:href'] = link
            
outputpath = path.join(outputdirectory, filename)
#write to file
with open(outputpath, 'w') as outfile:
          outfile.write(str(soup))