import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Dan", "Lina", "Tom"]
})

scores = pd.DataFrame({
    "student_id": [1, 1, 2, 3, 3],
    "subject": ["Math", "English", "Math", "Math", "English"],
    "score": [87, 90, 78, 92, 70]
})

print("=== Students ===")
print(students)

print("\n=== Scores ===")
print(scores)

print("\n=== Merge by student_id ===")
merged = pd.merge(students, scores, on="student_id")
print(merged)
