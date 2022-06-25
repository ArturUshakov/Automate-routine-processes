import pandas as pd
import plotly.express as px

excel_book_1_relative_path = 'Purchases - Home A.xlsx'
excel_book_prices = 'PriceBook.xlsx'

df_prices = pd.read_excel(excel_book_prices)
df_home_1 = pd.read_excel(excel_book_1_relative_path)

#print(df_prices, df_home_1)

df_total = df_home_1.merge(df_prices, on='ID')

df_total['Общая стоимость'] = df_total['Покупная сумма'] * df_total['Цена']

#print(df_total)

fig = px.pie(df_total[['Материал', 'Общая стоимость']],
             values='Общая стоимость', names='Материал')
fig.show()
