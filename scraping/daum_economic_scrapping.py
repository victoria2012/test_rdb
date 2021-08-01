from bs4 import BeautifulSoup
import requests

res = requests.get('http://media.daum.net/economic/')

import sqlite3
if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.select('a.link_txt')
    # with sqlite3.connect('./db.sqlite3') as conn
    connect = sqlite3.connect('../db.sqlite3')
    cursor = connect.cursor()
    # cursor.execute("create table daum_news(create_date, href, title)")  #이렇게 table을 만들 수도 있다

    for link in links:
        title = str.strip(link.get_text())
        href = str.strip(link.get('href'))
        try:
            cursor.execute(
                "insert into daum_news(create_date, href, title) values(datetime('now'), ?, ?)", (href,title))
            print(title, ' : ', href)

        except:
            pass

    connect.commit()