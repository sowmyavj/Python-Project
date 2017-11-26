import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
data = pd.read_csv('NewsHeadlinesNYC.csv', sep=',', na_values=".")
print data.shape
print data.columns
data.set_index('date',inplace=True)
#print data.head()

#
print data.sentiment

data['sentiment'].plot()
plt.legend()
plt.show()

#print data['pub_date'][0:10]
#print data[data['date'] == '3/1/2017']