import pandas as pd

df = pd.read_csv("day06/datasets/train.csv")

print("=== Rows & Columns ===")
print(df.shape)

print("\n=== First 5 rows ===")
print(df.head())
