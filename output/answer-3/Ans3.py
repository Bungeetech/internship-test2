data =pd.read_csv("intership_test2/input/question-3/main.csv")
d1 = {'Occupation':df['occupation'],'Age':df['age']}
df = pd.DataFrame(d1)
result = df.groupby('Occupation').agg({'age': ['min', 'max']})
print(result)
