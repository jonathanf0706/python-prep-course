import pandas as pd

# נטען CSV עם ערך חסר
df = pd.DataFrame({
    "name": ["Dan", "Tom", "Lina", "Ariel"],
    "age": [23, None, 21, 30],
    "score": [87, 92, None, 75]
})

print("=== original dataframe ===")
print(df)

# בדיקת ערכים חסרים
print("\n=== check for missing values ===")
print(df.isna())

# ספירת ערכים חסרים בכל עמודה
print("\n=== count missing values in each column ===")
print(df.isna().sum())

# מילוי ערכים חסרים
print("\n=== fill missing values (age mean, score 0) ===")
df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(0)

print(df)
