import pandas as pd

real = pd.read_csv("100 статей контроль.csv")
labeled = pd.read_csv("../Разметчик/разметка.csv")

acc = real['label'] == labeled['label']
print(acc.mean() * 100)
