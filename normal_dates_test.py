# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:01:18 2020

@author: ecphillips
"""

#import datetime
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
        for soup.unitdate in soup.find_all("unitdate"):
#            print(i)
            date = soup.unitdate.string
            #https://stackoverflow.com/questions/10115396/
            #how-to-test-if-an-attribute-exists-in-some-xml#10115420        
            if 'normal' in soup.unitdate.attrs:
                continue
            date = date[:7]             
            soup.unitdate.attrs['normal'] = date

# reformat the normal date
#            normal = datetime.datetime.strptime('%B %d, %Y').date()

# slice day off month-year dates
#            if date is [month-year = \w+\s+\d+ formatted]:
#                soup.unitdate.attrs['normal'][:7]

print(soup.prettify)