import pandas as pd

df = pd.read_excel("FRASES_A_QUECHUA.xlsx")
print("Total:", len(df))
print("Únicas:", df["Español"].nunique())
