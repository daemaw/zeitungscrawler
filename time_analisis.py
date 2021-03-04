# import csv
#
# with open('sz.csv', newline='') as csvfile:
#     sz = csv.reader(csvfile)
#     for row in sz:
#         print(row)
#
import pandas as pd
import matplotlib.pyplot as plt

dtypes = {'category' : 'str' , 'datetime' : 'str', 'title' : 'str', 'is_paywall' : 'bool'}
names = ['category', 'datetime', 'title', 'is_paywall']

data = pd.read_csv('sz.csv',
                        delimiter=',', names=names, dtype=dtypes,
                        parse_dates=['datetime'])

datetime = pd.to_datetime(data.datetime, utc=True)
#data['datetime'] = data['datetime'].astype('datetime64[ns]')
grp_data = data.groupby([datetime.dt.hour]).count()

plt.ylabel('Anzahl Artikel')

grp_data['title'].plot();
plt.xlabel('Tageszeit in h')
plt.show();