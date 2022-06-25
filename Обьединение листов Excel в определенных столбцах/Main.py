import os
import pandas as pd

data_location = "D:\VsCode\"
desired_headings = ["Важная информация"]
df_total = pd.DataFrame(columns=desired_headings)

for file in os.listdir(data_location):
    df_file = pd.read_excel(data_location + file)
    selected_columns = df_file.loc[:, desired_headings]
    df_total = pd.concat([selected_columns, df_total], ignore_index=True)

df_total.to_excel("ВажнаяИнформация.xlsx")
