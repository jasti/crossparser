'''
Created on Mar 27, 2013

@author: zudec
'''
from bs4 import BeautifulSoup
import urllib2

import urlGen

#response = urllib2.urlopen('http://www.pro-football-reference.com/play-index/play_finder.cgi?request=1&match=summary_all&year_min=2012&year_max=2012&team_id=chi&opp_id=&game_type=R&playoff_round=&game_num_min=1&game_num_max=1&week_num_min=0&week_num_max=99&quarter=1&quarter=2&quarter=3&quarter=4&quarter=5&tr_gtlt=lt&minutes=15&seconds=00&down=0&down=1&down=2&down=3&down=4&ytg_gtlt=gt&yds_to_go=&yg_gtlt=gt&yards=&is_first_down=-1&fp_gtlt=gt&fp_tm_opp=team&fp_ydline=&type=PASS&type=RUSH&is_turnover=-1&is_scoring=-1&no_play=0&game_day_of_week=&game_location=&game_result=&margin_min=&margin_max=&order_by=yards')

urls = urlGen.generateURL();
f = open('wods.txt','w')
for url in urls:
    
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
#print soup
    blogBodies = soup.findAll("div", {"class" : "blogbody"})

    for line  in blogBodies:
        f.write('\n-------------------------------------------------------------------\n');
        print('\n-------------------------------------------------------------------\n');
        workoutName = line.find("h3", {"class" : "title"})
        f.write(workoutName.text.split()[1]+'\n');
        print(workoutName.text.split()[1]+'\n');
        para =line.findAll('p')
        for p in para:
            if (p.text=='Enlarge image') |('Post' in p.text)|('comments' in p.text) :
                break;
            else:
                #print p.text;
                f.write(p.text+'\n')
                print p.text
          


