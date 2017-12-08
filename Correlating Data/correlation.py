import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import os

style.use('ggplot')

#create consolidated for News
data = pd.read_csv('Consolidated_Output.csv', sep=',', na_values=".")
#data = pd.read_csv('Consolidated_Output_total.csv', sep=',', na_values=".")
data['date'] = pd.to_datetime(data.date)
data["date"] = data["date"].dt.strftime("%m-%d-%Y")
data.set_index('date',inplace=True)

print "Corr news and tweets positive"
print data['positive_news'].corr(data['positive_tweets'])
print "*******************************\n\n"

print "Corr news and tweets negative"
print data['negative_news'].corr(data['negative_tweets'])
print "*******************************\n\n"

print "Corr negative news and tweets positive"
print data['negative_news'].corr(data['positive_tweets'])
print "*******************************\n\n"

print "Corr positive news and tweets negative"
print data['positive_news'].corr(data['negative_tweets'])
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
data=data.drop(['total_tweets','total_weather','total_news'],axis=1)
import numpy
names = ['positive_news','negative_news','positive_tweets','negative_tweets','positive_weather','negative_weather']
correlations = data.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,6,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names,rotation='vertical')
ax.set_yticklabels(names)
plt.show()
