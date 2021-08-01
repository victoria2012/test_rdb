# 판다스의 데이터를 DB에 넣고 읽어오는 연습

from sklearn import datasets
boston = datasets.load_boston()   # 변수 boston의 타입은 Bunch임.
                                  # Bunch 객체는 파이썬의 딕셔너리와 유사하며 keys()를 통해 키 목록 조회 가능
                                  # Bunch를 pandas로 바꿔줘야 데 DB에 넣어줄 때 좋다.

import pandas as pd
df = pd.DataFrame(boston['data'], columns=boston['feature_names'])

import sqlite3
connect = sqlite3.connect('../db.sqlite3')
df.to_sql('boston_table', connect, if_exists='append')   # 테이블이 없으면 테이블을 자동으로 만들어주는 기능

print(df)

connect.close()