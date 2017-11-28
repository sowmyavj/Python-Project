from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import os

style.use('ggplot')

#create consolidated for News
data = pd.read_csv('NewsHeadlinesNYC.csv', sep=',', na_values=".")
data['date'] = pd.to_datetime(data.date)
data["date"] = data["date"].dt.strftime("%m-%d-%Y")
data.set_index('date',inplace=True)

#print data.index
#print "##############################"

#create consolidated for News
wdata = pd.read_csv('climate_data_ny.csv', sep=',', na_values=".")
wdata['Date'] = pd.to_datetime(wdata['Date'])
wdata["Date"] = wdata["Date"].dt.strftime("%m-%d-%Y")
wdata.set_index('Date',inplace=True)
#print wdata.index

#create a list of all dates
dates=[]
for date in data.index:
    if(dates.count(date) == 0):
        dates.append(date)

#print dates
#print "##############################"
consolidated= pd.DataFrame(data=None,columns=["positive_news","negative_news","total_news","positive_tweets","negative_tweets","total_tweets",
"positive_weather","negative_weather","total_weather"],index=dates)
consolidated= consolidated.fillna(0.0)

for i in dates:
    newdates=data[data.index== i]
    positive=newdates[newdates["sentiment"]== 1]
    negative=newdates[newdates["sentiment"]== -1]
    consolidated['positive_news'].astype(float)
    if newdates.shape[0]!=0:
        #print positive.shape[0]/newdates.shape[0]
        consolidated.at[i, 'positive_news']=(positive.shape[0]/newdates.shape[0])
        #print consolidated.at[i, 'positive_news']
        consolidated.at[i, 'negative_news']=negative.shape[0]/newdates.shape[0]
        consolidated.at[i, 'total_news']=newdates.shape[0]

    wnewdates=wdata[wdata.index== i]
    wpositive=wnewdates[wnewdates["Weather Sentiment"]== 1]
    wnegative=wnewdates[wnewdates["Weather Sentiment"]== -1]
    if wnewdates.shape[0] != 0:
        
        consolidated.at[i, 'positive_weather']=wpositive.shape[0]/wnewdates.shape[0]
        consolidated.at[i, 'negative_weather']=wnegative.shape[0]/wnewdates.shape[0]
        consolidated.at[i, 'total_weather']=wnewdates.shape[0]
    
lists= os.listdir("./tweets_output_new/")
#print lists
for l in lists:
    data = pd.read_csv('./tweets_output_new/'+l, sep=',', na_values=".")
    data['Date'] = pd.to_datetime(data.Date)
    data["Date"] = data["Date"].dt.strftime("%m-%d-%Y")
    data.set_index('Date',inplace=True)
    i= data.index[0]
    positive=data[data["Sentiment"]== 1]
    negative=data[data["Sentiment"]== -1]
    if data.shape[0] != 0:
        print positive.shape[0]/data.shape[0]
        consolidated.at[i, 'positive_tweets']=positive.shape[0]/data.shape[0]
        consolidated.at[i, 'negative_tweets']=negative.shape[0]/data.shape[0]
        consolidated.at[i, 'total_tweets']=data.shape[0]
    #print data.index
    #print "##############################"

#print consolidated
consolidated.to_csv("Consolidated_Output.csv", encoding='utf-8')

