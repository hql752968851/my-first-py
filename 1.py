import    requests
from bs4   import BeautifulSoup
url="http://www.cntour.cn/"
response=requests.get(url)
#print(response.text)
soup=BeautifulSoup(response.text,'lxml')
data=soup.select("#main > article > div.kratos-hentry.kratos-post-inner.clearfix")
print(data)
for item in data;
    result={
    'title':item
}

