data= pd.read_csv('intership_test2/input/question-1/main.csv')
c = (data['year']//10)*10
X = data.drop(columns='year', axis=1)
Y = data['year']
X.drop('total', inplace=True, axis=1)
X.groupby(c).sum()
