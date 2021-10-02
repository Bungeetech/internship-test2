#Ques_2
d = pd.read_csv("intership_test2/input/question-2/main.csv")
data = {'Team':d['Team'],
        'Yellow Cards':d['Yellow Cards'],
        'Red Cards':d['Red Cards']}
k=pd.DataFrame(data)
df = k.sort_values(by=['Red Cards','Yellow Cards'])
df
