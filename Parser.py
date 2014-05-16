'''
Created on Mar 27, 2013

@author: zudec
'''
from bs4 import BeautifulSoup 
import requests
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import CrossparserUtils as cpu

#cpu.parseSite();

print "Finished writing to the file"

cols =['Date','Workout']
df = pd.read_csv('workouts.tsv', sep='\t', converters={'Date': str})  
df = df.dropna()

df['Year'], df['Month'], df['Day'] = zip(*df["Date"].map(cpu.splitDate))

print df
#dfRest=df[df.Workout== "Rest Day"]
dfRest = df[df['Workout'].str.contains("Rest Day") | df['Workout'].str.contains("Rest day")]


gb_year_month =dfRest.groupby(['Year','Month'])
print gb_year_month.size()

'''
for i, group in dfRest.groupby(['Year','Month']):
    plt.figure()
    group.plot(x='saleDate', y='MeanToDate', title=str(i))
'''
'''
df.dropna()
df[df['Workout'].str.contains("For time")]
'''
