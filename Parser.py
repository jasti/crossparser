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

urls = cpu.generateURL();
#print urls
f = open('wods.txt','w')

with open("workouts.tsv", "w") as f:
    fieldnames = ("Date", "Workout")
    output = csv.writer(f, delimiter="\t")
    output.writerow(fieldnames)
    
    
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        #print soup
        blogBodies = soup.findAll("div", {"class" : "blogbody"})
        for line  in blogBodies:
            #print('\n~break~\n');
          
            workoutName = line.find("h3", {"class" : "title"})
            #print workoutName
            if(len(workoutName.text.split()) < 2):
                # Some entries only have the day and not the actual date
                #workoutDate = np.nan;
                break;
            
            else:
                #Add 20 to the year part, so Pandas can easily extract the date format
                workoutDate = "20"+workoutName.text.split()[1];
          
            
            para =line.findAll('p')
            workout = "";
            for p in para:
                # Sometime their workouts have links and they need to be filtered for
                anchorExists = p.find("a")
                if (p.text=='Enlarge image') |('Post' in p.text)|('comments' in p.text)|(p.text == "") :
                    break;
                else:
                 
                    workout = workout+p.text.encode('utf-8')
                    
             
            output.writerow([workoutDate,workout.replace('\n',' ')])    
            #print "~~"
            #print workoutDate
            #print workout.rstrip('\n')



cols =['Date','Workout']
df = pd.read_csv('workouts.tsv', sep='\t', converters={'Date': str})  
df = df.dropna()

df['Year'], df['Month'], df['Day'] = zip(*df["Date"].map(cpu.splitDate))

print df
#dfRest=df[df.Workout== "Rest Day"]
print  df[df['Workout'].str.contains("Rest Day")]

'''
gb_year =dfRest.groupby('Year')
print gb_year.size()

df.dropna()
df[df['Workout'].str.contains("For time")]
'''
