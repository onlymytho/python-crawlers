import csv
import requests
from bs4 import BeautifulSoup
f = open('naver-webtoon.csv', 'w')
def spider():
    page = ['episode', 'omnibus', 'story', 'daily', 'comic', 'fantasy', 'action', 'drama', 'pure', 'sensibility', 'thrill', 'historical', 'sports']
    num = 0
    id =1
    while num < len(page) :
        url = 'http://comic.naver.com/webtoon/genre.nhn?genre=' + page[num]
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html5lib')
        for title_list in soup.find_all(['a', 'strong']):
            title = title_list.text
            genre = page[num]
            f.write(title+',')

        num += 1
        #href = url
        #print(href)
            

spider()
f.close()
print('successfully done')
