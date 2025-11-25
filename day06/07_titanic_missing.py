import pandas as pd

df = pd.read_csv("day06/datasets/train.csv")

print("=== Missing Values Count ===")
print(df.isna().sum())
