import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://news.yahoo.co.jp/topics'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all('div', class_='list')
    for sponsor in sponsors:
        for news_title in sponsor.ul:

            #ここでは、改行orliタグが入ってくる。改行の時は、処理しないように除外をしたい
            #print(news_title)


            if news_title!= "\n":
                print(news_title.text)
               # import pdb;pdb.set_trace()




            # print(news_title.li.a.text)

            # url = sponsor.ul.li.a['href']
            # name = sponsor.ul.li.a.text

            #print(name, url)
            #name = sponsor.h4.text
            #print(name, url)


if __name__ == '__main__':
    main()
