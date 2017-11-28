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

print "Corr news and weather positive"
print data['positive_news'].corr(data['positive_weather'])
print "*******************************\n\n"

print "Corr news and weather negative"
print data['negative_news'].corr(data['negative_weather'])
print "*******************************\n\n"