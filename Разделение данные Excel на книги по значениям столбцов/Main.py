import pandas as pd

excel_file_path = 'Лист Microsoft Excel.xlsx'

df = pd.read_excel(excel_file_path)
# print(df)

split_values = df['Смена'].unique()
# print(split_values)

for value in split_values:
    df1 = df[df['Смена'] == value]
    output_file_name = "Смена_" + str(value) + "_Trainings.xlsx"
    df1.to_excel(output_file_name, index=False)
