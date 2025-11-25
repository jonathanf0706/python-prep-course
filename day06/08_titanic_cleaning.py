import pandas as pd

df = pd.read_csv("day06/datasets/train.csv")

# 1. הורדת עמודות עם הרבה חסרים
df = df.drop(columns=["Cabin"])

# 2. מילוי גיל חסר לפי ממוצע
df["Age"] = df["Age"].fillna(df["Age"].mean())

# 3. מילוי ערכי Embarked חסרים (בדרך כלל 2)
df["Embarked"] = df["Embarked"].fillna("S")

# 4. בדיקה אחרונה
print(df.isna().sum())
