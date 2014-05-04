'''
Created on Mar 27, 2013

@author: zudec
'''
from bs4 import BeautifulSoup
import urllib2
import codecs
import re

#response = urllib2.urlopen('http://www.pro-football-reference.com/play-index/play_finder.cgi?request=1&match=summary_all&year_min=2012&year_max=2012&team_id=chi&opp_id=&game_type=R&playoff_round=&game_num_min=1&game_num_max=1&week_num_min=0&week_num_max=99&quarter=1&quarter=2&quarter=3&quarter=4&quarter=5&tr_gtlt=lt&minutes=15&seconds=00&down=0&down=1&down=2&down=3&down=4&ytg_gtlt=gt&yds_to_go=&yg_gtlt=gt&yards=&is_first_down=-1&fp_gtlt=gt&fp_tm_opp=team&fp_ydline=&type=PASS&type=RUSH&is_turnover=-1&is_scoring=-1&no_play=0&game_day_of_week=&game_location=&game_result=&margin_min=&margin_max=&order_by=yards')
response = urllib2.urlopen('http://www.crossfit.com/mt-archive2/2012_05.html')

html = response.read()
soup = BeautifulSoup(html)
#print soup
blogBodies = soup.findAll("div", {"class" : "blogbody"})

for line  in blogBodies:
    workoutName = line.find("h3", {"class" : "title"})
    print workoutName.text.split()[1];
    
    para =line.findAll('p')
    for p in para:
        if (p.text=='Enlarge image') |(p.text=='Post time to comments.') | (p.text=='Post loads to comments.')|(p.text=='Post total to comments.'):
            break;
        else:
            print p.text;
    
    
    


#print (unicode.join(u'\n',map(unicode,tabulka)))
#print '-----------------------------------------------------------------------------'
#print tabulka

