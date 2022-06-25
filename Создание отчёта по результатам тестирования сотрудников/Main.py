import numpy as np
import pandas as pd

scores_df = pd.read_excel('Тесты.xlsx')
# print(scores_df)

scores_df['среднее число'] = scores_df.mean(axis=1)

#scores_df['Pass/Fail'] = np.where(scores_df['среднее число'] > 60, 'Pass', 'Fail')
# print(scores_df)

conditions = [
    (scores_df['среднее число'] >= 90),
    (scores_df['среднее число'] < 90) & (scores_df['среднее число'] >= 80),
    (scores_df['среднее число'] < 80) & (scores_df['среднее число'] >= 70),
    (scores_df['среднее число'] < 70) & (scores_df['среднее число'] >= 60),
    (scores_df['среднее число'] < 60)
]
results = ['A', 'B', 'C', 'D', 'F']

scores_df['буквенная оценка'] = np.select(conditions, results)
# print(scores_df)

scores_df['Допуск/Провал'] = ['Допуск' if x >
                              60 else 'Провал' for x in scores_df['среднее число']]
df_all = pd.concat([scores_df])
df_all.to_excel("Отчёт по тестам.xlsx")
print(scores_df)
