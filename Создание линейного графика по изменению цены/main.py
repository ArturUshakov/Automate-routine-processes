import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df_excel = pd.read_excel('ежемесячные цены на материалы.xlsx')

# Viewing data
print(df_excel.tail(20))

dates = df_excel['Дата']
prices = df_excel['Цена']

# simple operations
df_excel['Цена покупки'] = prices * .9
print(df_excel['Цена'].max())
df_excel['Дата'] = df_excel['Дата'].str.replace('-', '.')

df_all = pd.concat([df_excel])
print(df_excel)
df_all.to_excel("Отчёт по месячным затратам.xlsx")

fig = px.line(df_excel, x = dates, y = prices, title = 'Цена покупки за всё время')
fig.show()
