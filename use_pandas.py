import pandas as pd

table = pd.read_csv("ibadan_north_wards.csv")

print(table.head())
print("Rows:", len(table))
