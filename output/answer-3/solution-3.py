import pandas as pd
df = pd.read_csv('../../input/question-3/main.csv')
df[['Team', 'Yellow Cards', 'Red Cards']].sort_values(
    by=['Red Cards'], ascending=False).to_csv('answer-3.csv', index=False)
