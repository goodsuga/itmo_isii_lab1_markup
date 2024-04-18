import pandas as pd

input_file = pd.read_csv("Полный ДС с разметкой.csv")
input_file.iloc[:100].drop(columns=["label"]).to_csv("100 статей неразмеченные.csv", index=False)
input_file.iloc[:100].to_csv("100 статей контроль.csv", index=False)
