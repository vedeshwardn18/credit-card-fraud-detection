import pandas as pd

df = pd.read_csv("database/creditcard.csv")

fraud_rows = df[df["Class"] == 1]

print(fraud_rows.head(1))