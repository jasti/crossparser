# -*- coding: utf-8 -*-
"""
Created on Thu May 15 11:00:58 2014

@author: vjasti
"""

from datetime import datetime
import calendar

# Generates URLS that need to be queried for workouts
def generateURL():
    crossfitBaseUrl = 'http://www.crossfit.com/mt-archive2/YYYY_MM.html'
    yearRange = range(2002, 2003)
    # monthRange = ['01','02','03','04','05','06','07','08','09','10','11','12']
    monthRange = ['01']
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
   
        

    
    
