import requests
from bs4 import BeautifulSoup

url = "http://mignews.com/mobile/"

source = requests.get(url)
print(source.status_code)

new_news = []
news = []

soup = BeautifulSoup(source.text, 'html.parser')

news = soup.findAll('a', class_ ='lenta')

for chtougodno in range(len(news)):
    if news[chtougodno].find('span', class_ ='time2 time3') is not None:
        new_news.append(news[chtougodno].text)

for i in range(len(new_news)):
    print(new_news[i])