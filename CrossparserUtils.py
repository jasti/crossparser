# -*- coding: utf-8 -*-
"""
Created on Thu May 15 11:00:58 2014

@author: vjasti
"""

from datetime import datetime
import calendar
import numpy as np
from bs4 import BeautifulSoup 
import requests
import csv

# Generates URLS that need to be queried for workouts
def generateURL():
    crossfitBaseUrl = 'http://www.crossfit.com/mt-archive2/YYYY_MM.html'
    yearRange = range(2002, 2014)
    monthRange = ['01','02','03','04','05','06','07','08','09','10','11','12']
    #monthRange = ['01']
    crossfitUrls = [];
    for year in yearRange:
        for month in monthRange:
            crossfitYearUrl = crossfitBaseUrl.replace('YYYY', str(year))
            crossfitUrl = crossfitYearUrl.replace('MM', str(month))
            crossfitUrls.append(crossfitUrl);
    return crossfitUrls  




def splitDate(date):
    # print type(date)
    strDate = str(date);
    # print strDate
    try:
        mydate = datetime.strptime(strDate, '%Y%m%d')
        # mydate = datetime.strptime(strDate,'%Y-%m-%d %H:%M:%S')
        
        return [mydate.year, calendar.month_name[mydate.month], mydate.day]
    except ValueError:
        print "Bad Date encountered : " + strDate
        return [np.NaN,np.NaN,np.NaN]
    
def parseSite():
    urls = generateURL();
#print urls

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
                if workoutName is not None:
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
                    print "~~" 
                    print workoutDate
                    print workout.rstrip('\n')
    
   
        

    
    
