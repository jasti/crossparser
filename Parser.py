'''
Created on Mar 27, 2013

@author: zudec
'''
import csv

from bs4 import BeautifulSoup 
import requests

import CrossparserUtils as cpu
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#cpu.parseSite();
print "Finished writing to the file"

cols =['Date','Workout']
df = pd.read_csv('workouts_2005.tsv', sep='\t', converters={'Date': str})  
df = df.dropna()

df['Year'], df['Month'], df['Day'] = zip(*df["Date"].map(cpu.splitDate))

print df


#Workouts per year
df_year_total=df.groupby(['Year']).size()
print "Total workouts per year : "
print df_year_total

cpu.writeToFile('output/workouts_total_2005.tsv',['Year','Count'],'\t',cpu.listFromDf(df_year_total))


#Calculate Rest days per year
dfRest = df[df['Workout'].str.contains("Rest Day") | df['Workout'].str.contains("Rest day")]
print dfRest.reset_index(inplace=True)
df_year_rest=dfRest.groupby(['Year']).size()
print "Rest days per Year : "
print df_year_rest
cpu.writeToFile('output/workouts_rest.tsv',['Year','Count'],'\t',cpu.listFromDf(df_year_rest))

#Calculate for time days per year

dfTime = df[df['Workout'].str.contains("For Time:") | df['Workout'].str.contains("For time:")]
print dfTime.reset_index(inplace=True)
df_year_time=dfTime.groupby(['Year']).size()
print "For time workouts per Year : "
print df_year_time
cpu.writeToFile('output/workouts_for_time.tsv',['Year','Count'],'\t',cpu.listFromDf(df_year_time))

# Calculate for rounds per year

dfRounds = df[df['Workout'].str.contains("As many rounds") | df['Workout'].str.contains("as many rounds")]
print dfRounds.reset_index(inplace=True)
df_year_rounds=dfRounds.groupby(['Year']).size()
print "For Round workouts per Year : "
print df_year_rounds
cpu.writeToFile('output/workouts_rounds.tsv',['Year','Count'],'\t',cpu.listFromDf(df_year_rounds))

# Calculate Hero wods per year

dfHero = df[df['Workout'].str.contains("\"\"\"")]
print dfHero.reset_index(inplace=True)
df_hero_year=dfHero.groupby(['Year']).size()
print "Hero WODS per year : "
print df_hero_year
cpu.writeToFile('output/workouts_hero.tsv',['Year','Count'],'\t',cpu.listFromDf(df_hero_year))

