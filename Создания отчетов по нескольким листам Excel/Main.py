import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = 'данные первой и второй смены.xlsx'
excel_file_2 = 'данные третьей смены.xlsx'

df_first_shift = pd.read_excel(excel_file_1, sheet_name='Первая')
df_second_shift = pd.read_excel(excel_file_1, sheet_name='Вторая')
df_third_shift = pd.read_excel(excel_file_2)



df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])

pivot = df_all.groupby(['Смена']).mean()
shift_productivity = pivot.loc[:,
                               "Время производственного прогона (мин.)":"Произведенные продукты (единицы)"]

print(shift_productivity)


df_all.to_excel("Продукция.xlsx")
