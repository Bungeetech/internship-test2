import pandas as pd
df_c = pd.read_csv('../../input/question-1/main.csv')
new_df = pd.DataFrame(columns=df_c.columns)
i = 0
for df in pd.read_csv('../../input/question-1/main.csv', iterator=True, chunksize=10):
    new_df.loc[i] = df.sum(axis=0)
    new_df.loc[i]['Year'] = df.reset_index()['Year'][0]
    new_df.loc[i]['Population'] = df.reset_index(
    )['Population'][len(df.reset_index()['Population']) - 1]
    i += 1

new_df.drop(['Total'], axis=1).to_csv('answer-1.csv', index=False)
