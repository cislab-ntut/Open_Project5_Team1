import requests
res = requests.get('http://www.wibibi.com/info.php?tid=116')
#print(res.text)
res.encoding = 'utf-8' #'big5'
#print(res.text)

f = open('test.html','w',encoding='utf-8')
f.write(res.text)
f.close()

import pandas as pd
dfs = pd.read_html('test.html')
print(dfs[3])