import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

# assign url to cnn top stories
url = "http://rss.cnn.com/rss/cnn_topstories.rss"
def news_rss(url):
    article_list = []
    try:
        # send get request
        r = requests.get(url)
        content = BeautifulSoup(r.content, features='xml')
        articles = content.findAll('item')

        # pull title and link from response
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text

            article = {
                'title': title,
                'link': link,
            }
            # article info to array
            article_list.append(article)

        return save_func(article_list)
    except Exception as e:
        print('The scraping job failed. Error: ')
        print(e)

# create .txt file in articles directory and populate with articles
def save_func(article_list):
    unique = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    filename = 'article'+unique+'.txt'
    with open(f'articles/{filename}', 'w') as f:
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
