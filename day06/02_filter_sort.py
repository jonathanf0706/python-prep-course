import pandas as pd

df = pd.read_csv("day06/students.csv")

print("=== filter example by age > 20 ===")
filtered = df[df["age"] > 20]
print(filtered)

print("\n=== sort example by score from high to low ===")
sorted_df = df.sort_values(by="score", ascending=False)
print(sorted_df)
