import pandas as pd

# יצירת Series
s = pd.Series([10, 20, 30])
print("Series:")
print(s)

# יצירת DataFrame
df = pd.DataFrame({
    "name": ["Dan", "Tom"],
    "age": [23, 19],
    "score": [87, 92]
})

print("\nDataFrame:")
print(df)
