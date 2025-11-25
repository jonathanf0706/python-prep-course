import pandas as pd

df = pd.DataFrame({
    "student": ["Dan", "Dan", "Lina", "Lina", "Tom"],
    "subject": ["Math", "English", "Math", "English", "Math"],
    "score": [87, 90, 78, 85, 92]
})

print("=== Data ===")
print(df)

print("\n=== average for each subject ===")
grouped = df.groupby("subject")["score"].mean()
print(grouped)

print("\n=== average by student and subject ===")
grouped = df.groupby(["student", "subject"])["score"].mean()
print(grouped)