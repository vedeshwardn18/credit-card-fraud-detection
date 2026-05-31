import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("database/creditcard.csv")

fraud_row = df[df["Class"] == 1].head(1)

print(fraud_row.to_string())