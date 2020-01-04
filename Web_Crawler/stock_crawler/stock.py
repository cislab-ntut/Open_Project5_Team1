import requests
response = requests.get('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20191009&type=ALLBUT0999&_=1570793617643')
#print(response.text[:1000])
lines = response.text.split("\n")
#print(lines[300])

newlines = []

for line in lines:
    if len(line.split('",')) == 17:
        newlines.append(line)
#print(newlines[1])

import pandas as pd
from io import StringIO

df = pd.read_csv(StringIO("\n".join(newlines).replace('=','')))
#print(df.head())

df = df.astype(str)

df = df.apply(lambda s:s.str.replace(",",""))

df = df.set_index('證券代號')
#print(df.head())
#print(df.loc['0050'])

df = df.apply(lambda s:pd.to_numeric(s, errors='coerce'))
#print(df.head())

df = df[df.columns[df.isnull().sum() != len(df)]]
#print(df.head())

#print(df[df['收盤價']/df['開盤價'] > 1.05])

#df = pd.read_csv(StringIO(response.text))
#print(df)

#存檔 csv
df.to_csv('daily_price.csv',encoding='utf_8_sig')
df = pd.read_csv('daily_price.csv', index_col=['證券代號'],)
df = df.loc[~df['收盤價'].isnull()]
#print(df)
