'''
Created on May 23, 2013

@author: zudec
'''

def generateURL():
    crossfitBaseUrl = 'http://www.crossfit.com/mt-archive2/YYYY_MM.html'
    yearRange = range(2006,2015)
    monthRange = ['01','02','03','04','05','06','07','08','09','10','11','12']
    crossfitUrls=[];
    for year in yearRange:
        for month in monthRange:
            crossfitYearUrl =crossfitBaseUrl.replace('YYYY', str(year))
            crossfitUrl=crossfitYearUrl.replace('MM',str(month))
            crossfitUrls.append(crossfitUrl);
    return crossfitUrls  


