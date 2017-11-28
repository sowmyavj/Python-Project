#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 00:59:51 2017

@author: sowmyav
"""
import urllib2
from bs4 import BeautifulSoup

def getPMHour(_hour):
	if(_hour=='12'):
		return "12"
	return (int(_hour) +12)

def getAMHour(_hour):
	if(_hour=='12'):
		return "00"
	return (int(_hour))


f=open("climate_data_ny.csv",'w');
f.write("Date,Hour,Min,Temp,Conditions,Weather Sentiment"+'\n')

#Change the range according to month range required. eg: For month of Jan and feb use range(1,3)
for m in range(1,13):
    if len(str(m)) < 2:
        mStamp='0' + str(m)
    else:
        mStamp=str(m)

    for d in range(1,32):
        if len(str(d)) < 2:
            dStamp='0' + str(d)
        else:
            dStamp=str(d)
        #
         
        if(m==2 and d>28):
            break
        if(m in [4,6,9,11] and d > 30):
            break
        timestamp='2017/'+str(m)+'/'+str(d)
        
        print "getting data for "+timestamp
        url="https://www.wunderground.com/history/airport/KNYC/"+timestamp+"/DailyHistory.html?req_city=New%20York&req_state=NY&req_statename=New%20York&reqdb.zip=10001&reqdb.magic=8&reqdb.wmo=99999"
        #url="https://www.wunderground.com/history/airport/KNYC/2017/1/1/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&reqdb.zip=10001&reqdb.magic=8&reqdb.wmo=99999"

        page=urllib2.urlopen(url);
                           
        soup=BeautifulSoup(page,"lxml");
        i=soup.find_all(attrs={"class":"obs-table responsive"})

        for t in i:
            if t.find_all('th')[11].text == "Conditions":
                index_of_conditions=11
            else:
                index_of_conditions=12
            wx=soup.find_all(attrs={"class":"no-metars"})

        for temp in wx:
            conditions= temp.find_all('td')[index_of_conditions].text.encode('utf-8').strip()
            if conditions in ["Clear","Light Rain"]:
                weather_sentiment=1
            elif conditions in ["Partly Cloudy","Haze","Scattered Clouds","Fog","Mist","Unknown"]:
                weather_sentiment=0
            elif conditions in ["Light Snow","Mostly Cloudy","Overcast","Snow","Rain","Heavy Rain","Heavy Snow","Light Freezing Rain","Light Freezing Fog"]:
                weather_sentiment=-1
            else:
                weather_sentiment=conditions

            hour_text=  temp.find_all('td')[0].text
            #print hour_text
            hoursplit =hour_text.split();
            hour_min= hoursplit[0].strip()
            am_pm=hoursplit[1].strip()
            hour=hour_min.split(":")[0]
            minute=hour_min.split(":")[1]

            
            if (am_pm == 'PM'):
            	hour=str(getPMHour(hour))
            elif(am_pm == 'AM'):
            	hour=str(getAMHour(hour))
           
           	
            #print "hr:"+hour
            #print "min:"+min
            #temperature=  temp.find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text
            temperature = "NA" if (temp.find_all('td')[1].find_all(attrs={"class":"wx-value"})==[]) else temp.find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text
            #print temperature
            #print temp.find_all('td')[0].text,temp.find_all('td')[1].text,temp.find_all('td')[12].text
            date=mStamp+'/'+dStamp+'/2017'
            #f.write(date+','+str(hour)+','+str(temp)+','+str(conditions)+'\n')
            # f.write(date+','+hour.encode('utf-8').strip()+','+temperature.encode('utf-8').strip()+','+str(conditions)+','+str(weather_sentiment)+'\n')
            f.write(date+','+hour.encode('utf-8').strip()+','+minute.encode('utf-8').strip()+','+temperature.encode('utf-8').strip()+','+str(conditions)+','+str(weather_sentiment)+'\n')
f.close()

'''
timestamp="2017/3/8"
url="https://www.wunderground.com/history/airport/KNYC/"+timestamp+"/DailyHistory.html?req_city=New%20York&req_state=NY&req_statename=New%20York&reqdb.zip=10001&reqdb.magic=8&reqdb.wmo=99999"
#url="https://www.wunderground.com/history/airport/KNYC/2017/1/12/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&reqdb.zip=10001&reqdb.magic=8&reqdb.wmo=99999"
#url="https://www.wunderground.com/history/airport/KNYC/2017/1/12/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&reqdb.zip=10001&reqdb.magic=8&reqdb.wmo=99999"
print url
page=urllib2.urlopen(url);
                           
soup=BeautifulSoup(page,"lxml");
i=soup.find_all(attrs={"class":"obs-table responsive"})

for t in i:
    if t.find_all('th')[11].text == "Conditions":
        index_of_conditions=11
    else:
        index_of_conditions=12

wx=soup.find_all(attrs={"class":"no-metars"})

for temp in wx:

    conditions= temp.find_all('td')[index_of_conditions].text.encode('utf-8').strip()
    if conditions in ["Clear","Light Rain"]:
        weather_sentiment="positive"
    elif conditions in ["Partly Cloudy","Haze","Scattered Clouds","Fog","Mist","Unknown"]:
        weather_sentiment="neutral"
    elif conditions in ["Light Snow","Mostly Cloudy","Overcast","Snow","Rain","Heavy Rain","Heavy Snow","Light Freezing Rain"]:
        weather_sentiment="negative"
    else:
        weather_sentiment=conditions

    hour=  temp.find_all('td')[0].text
    print "hour"+hour
    #print temp.find_all('td')[1].find_all(attrs={"class":"wx-value"})
    temperature = "NA" if (temp.find_all('td')[1].find_all(attrs={"class":"wx-value"})==[]) else temp.find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text
    print hour,temperature,conditions,weather_sentiment
    #temperature=  temp.find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text

'''
print "finished getting data."
#print wx