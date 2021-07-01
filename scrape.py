import requests
import json
from bs4 import BeautifulSoup

url = "http://rss.cnn.com/rss/cnn_topstories.rss"
def news_rss(url):
    article_list = []
    try:
        r = requests.get(url)
        content = BeautifulSoup(r.content, features='xml')
        articles = content.findAll('item')

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text

            article = {
                'title': title,
                'link': link,
            }
            article_list.append(article)

        return save_func(article_list)
    except Exception as e:
        print('The scraping job failed. Error: ')
        print(e)

def save_func(article_list):
    with open('articles.txt', 'w') as f:
        for a in article_list:
            f.write(a['title'])
            f.write('\n')
            f.write(a['link'])
            f.write('\n')
            f.write('\n')
        f.close



print('Gathering articles...')
news_rss(url)
print('Articles compiled')
