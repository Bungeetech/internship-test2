import pandas as pd
df = pd.read_csv('../../input/question-2/main.csv')
gb = df.groupby('occupation').agg({'age': ['min', 'max']})
gb.to_csv('answer-2.csv', index=False)
