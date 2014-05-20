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
df = pd.read_csv('workouts_2005_HERO.tsv', sep='\t', converters={'Date': str})  
df = df.dropna()

df['Year'], df['Month'], df['Day'] = zip(*df["Date"].map(cpu.splitDate))

print df



dfHero = df[df['Workout'].str.contains("HERO:")]
print dfHero.reset_index(inplace=True)
df_hero_year=dfHero.groupby(['Year']).size()
print "Hero WODS per year : "
print df_hero_year
cpu.writeToFile('output/workouts_hero.tsv',['Year','Count'],'\t',cpu.listFromDf(df_hero_year))

