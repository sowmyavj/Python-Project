import csv
import json
import os
from collections import OrderedDict
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

#nltk.download('vader_lexicon')
lists= os.listdir("./simplified/")
#print lists

sia = SIA()
pos_list = []
neg_list = []
pos=0
neg=0
total=0

output = csv.writer(open("WeatherDataNYC.csv", "ab"))
first=True

for f in lists:
    with open("./simplified/"+f) as data_file:    
        data = json.load(data_file)

    #print first
    if first is True:
        output.writerow(["Impact", "headline","isMajor","web_url","_id", "pub_date"  ])
        first=False
    
    for row in data["data"]:
        myrow=row
        for r in myrow:
            #print r
            if r != "keywords":
                row[r]=myrow[r].encode("utf-8")
        res = sia.polarity_scores(row["headline"])
        total=total+1
        newrow=myrow
        if res['compound'] > 0.2:
            newrow["Impact"] = "positive"
        elif res['compound'] < -0.2:
            newrow["Impact"] = "negative"
        else:
            newrow["Impact"] = "none"
        output.writerow(newrow.values())
            


