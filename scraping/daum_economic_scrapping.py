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

    data = []
    for link in links:
        title = str.strip(link.get_text())
        href = str.strip(link.get('href'))
        try:
            cursor.execute(
                "insert into polls_economics(create_date, href, title) values(datetime('now'), ?, ?)", (href,title))
            # print(title, ' : ', href)
            news = [title, href]
            data.append(news)
        except:
            pass

print(data)
import pandas as pd

df = pd.Dataframe(data)

connect = sqlite3.connect('../db.sqlite3')
df.to_sql('polls_economics', connect, if_exists='append')  # 테이블이 없으면 테이블을 자동으로 만들어주는 기능

print(df)

connect.close()
connect.commit()



