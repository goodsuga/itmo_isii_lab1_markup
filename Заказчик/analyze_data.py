import pandas as pd

data = pd.read_csv("Полный ДС с разметкой.csv")
print(data['label'].describe())
print(data['label'].n_unique())

