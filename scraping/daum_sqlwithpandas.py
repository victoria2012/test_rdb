import sqlite3

connect = sqlite3.connect('./db.sqlite3')

import pandas as pd

df_mask = pd.read_sql_query("select * from polls_economics where title like '%마스크%'", connect)
df_labor = pd.read_sql_query("select * from polls_economics where title like '%노동%'", connect)
df_income = pd.read_sql_query("select * from polls_economics where title like '%소득%'", connect)

df_mask.to_sql('daum_mask', connect, if_exists='replace')
df_labor.to_sql('daum_labor', connect, if_exists='replace')
df_income.to_sql('daum_income', connect, if_exists='replace')

connect.close()