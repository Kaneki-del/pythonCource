import requests
from bs4 import BeautifulSoup
url = 'https://news.ycombinator.com/news'
res = requests.get(url)
if res.status_code == 200:
    print(res.text)
else: 
    print('somting went wrong')
