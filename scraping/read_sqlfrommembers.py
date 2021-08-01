# 판다스로 데이터 불러오기

import sqlite3
connect = sqlite3.connect('../db.sqlite3')

import pandas as pd
df = pd.read_sql_query('select * from members where age >= 25', connect)

connect.close()
