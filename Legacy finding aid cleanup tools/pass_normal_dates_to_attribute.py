# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:17:54 2021

@author: eliza
"""
# Add missing normal dates

from bs4 import BeautifulSoup
import os
from os import path
import datetime
import re

directory = '/Users/ecphillips/staging'
outputdirectory = '/Users/ecphillips/cleaned'

for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        xmlfile = path.join(directory, filename)
        with open(xmlfile, 'r') as file:
            soup = BeautifulSoup(file, "lxml-xml")

# pass the date to the attribute            
# https://stackoverflow.com/questions/63744550/beautifulsoup-xml-parsing-only-return-first-result            

            for soup.unitdate in soup.find_all("unitdate"):
                date = soup.unitdate.string       
                #https://docs.python.org/3/library/re.html
                month_year = re.compile(r"(([a-zA-Z]+) (\d{4}))")
                month_day_year = re.compile(r"(([a-zA-Z]+) (\d+), (\d{4}))")
                multi_year = re.compile(r"(\d{4})-(\d{4})")
                single_year = re.compile(r"(\d{4})")
                if date == "Undated":
                    date = "undated"
                if date == "undated":
                    soup.unitdate.attrs['normal'] = "0000"
                if 'normal' in soup.unitdate.attrs:
                    continue
                #https://stackabuse.com/converting-strings-to-datetime-in-python/
                for date2 in re.findall(month_year, date):
                    date2 = datetime.datetime.strptime(date, "%B %Y")
                    date3 = datetime.date.strftime(date2, "%Y-%m")
                    soup.unitdate.attrs['normal'] = date3
                for date2 in re.findall(month_day_year, date):
                    date2 = datetime.datetime.strptime(date, "%B %d, %Y")
                    date3 = datetime.date.strftime(date2, "%Y-%m-%d")
                    soup.unitdate.attrs['normal'] = date3
                for date2 in re.findall(single_year, date):
                    soup.unitdate.attrs['normal'] = date2

#multi-year needs to be handled as a tuple
#https://codedestine.com/python-tuple-string-convert/

                for date2 in re.findall(multi_year, date):
                    separator = "/"
                    soup.unitdate.attrs['normal'] = separator.join(date2)


#print(soup.prettify)
outputpath = path.join(outputdirectory, filename)
#write to file
with open(outputpath, 'w') as outfile:
          outfile.write(str(soup))
