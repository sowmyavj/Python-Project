import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import os

style.use('ggplot')

#create consolidated for News
data = pd.read_csv('Consolidated_Output.csv', sep=',', na_values=".")
data['date'] = pd.to_datetime(data.date)
data["date"] = data["date"].dt.strftime("%m-%d-%Y")
data.set_index('date',inplace=True)

print "Corr news and tweets positive"
print data['positive_news'].corr(data['positive_tweets'])
print "*******************************\n\n"

print "Corr news and tweets negative"
print data['negative_news'].corr(data['negative_tweets'])
print "*******************************\n\n"

print "Corr weather and tweets positive"
print data['positive_weather'].corr(data['positive_tweets'])
print "*******************************\n\n"

print "Corr weather and tweets negative"
print data['negative_weather'].corr(data['negative_tweets'])
print "*******************************\n\n"

print "Corr news negative and tweets positive"
print data['negative_news'].corr(data['positive_tweets'])
print "*******************************\n\n"