import unicodecsv as csv
import json
import os
from collections import OrderedDict
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from datetime import datetime

#nltk.download('vader_lexicon')
lists= os.listdir("./simplified/")
lists1= os.listdir("./news/")
#print lists

sia = SIA()
pos_list = []
neg_list = []
pos=0
neg=0
total=0

output = csv.writer(open("NewsHeadlinesNYC.csv", "ab"))
first=True

for l in lists1:
    with open("./news/"+l) as data_file:  
       data = json.load(data_file)
       if first is True:
        output.writerow(["date_hour","date_min","sentiment", "web_url", "date","id"  ])
        first=False
    for row in data["response"]["docs"]:
        myrow={}
        res = sia.polarity_scores(row["headline"]["main"])
        date=row["pub_date"][0:10]
        date1=row["pub_date"][11:13]
        date2=row["pub_date"][14:16]
        myrow["date"]=date
        myrow["date_hour"]=date1
        myrow["date_min"]=date2
        myrow["web_url"]=row["web_url"]
        myrow["id"]=row["_id"]
        if res['compound'] > 0.2:
            myrow["sentiment"] = "positive"
        elif res['compound'] < -0.2:
            myrow["sentiment"] = "negative"
        else:
            myrow["sentiment"] = "none"
        output.writerow(myrow.values())



