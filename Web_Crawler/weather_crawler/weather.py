import requests
response = requests.get('https://www.cwb.gov.tw/V8/C/C/Statistics/monthlydata.html')
#print(response.text[:1000])
response.encoding = 'utf-8'
f = open('test.html','w',encoding='utf-8')
f.write(response.text)
f.close()

print(response.text)
import pandas as pd