from sklearn import datasets
boston = datasets.load_boston()

import pandas as pd
df = pd.DataFrame(boston['data'], columns=boston['feature_names'])

import sqlite3
connect = sqlite3.connect('../db.sqlite3')
df.to_sql('boston_table', connect, if_exists='append')   # 테이블이 없으면 테이블을 자동으로 만들어주는 기능

print(df)

connect.close()