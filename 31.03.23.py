rtdhfgcv
import threading
import time
import requests
from bs4 import BeautifulSoup as bs
dasdasdasdas
a = []

def parse(lst):
    for i in lst:
        soup = bs(1, 'html.parser')
        res = soup.find_all("articles")
        for j in res:
            print(j.getText())
    
def main(link):
    response = requests.get(link)
    a.append(response.text)

    c1 = time.time()

    t1 = threading.Thread(target = main, args = ("https://lenta.ru/rss/news",))

    t1.start()

    t1.join()
    parse(a)

    print(time.time() - c1)