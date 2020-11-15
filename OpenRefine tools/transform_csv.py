#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:30:51 2020

@author: dan, mainly
"""
# Reformat ASpace ingest CSV exported from OpenRefine to XLSX and add
# a blank row before first data row (stands in for second header row
# in plugin template)

from glob import glob
import pandas as pd
from os import path

fileList=glob("C:/Users/ecphillips/box_lists/*.csv")
for file in fileList:
    df = pd.read_csv(file)
    #makes new empty record - adding a blank row:
    # make dataframe - iloc is index location, colon is wildcard
    # .to_frame() turns it back into a 2 dimensional dataframe
    #.T transposes
    blankLine = df.iloc[0,:].to_frame().T
    #print("line contents", blankLine)
    #for everything in blankLine, replace with empty string
    #.loc would also work here
    blankLine.iloc[:,:] = ""
    #replace dataframe with appended version
    df = blankLine.append(df)
    #output file, full path:
    directory="C:/Users/ecphillips/box_lists_transformed/"
    newfilename=path.basename(file).replace(".csv", ".xlsx")
    newpath=path.join(directory, newfilename)
    df.to_excel(newpath, index=False)
#    print(newpath)