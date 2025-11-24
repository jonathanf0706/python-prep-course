import numpy as np

# השורה הזאת מאתחלת את הגנרטור של המספרים האקראיים כך שהתוצאות יהיו תמיד אותו דבר בין ריצות
# בחרנו דווקא את המספר 42 כי זה ערך דוגמה מקובל שתמיד חוזר במדריכים (וגם בגלל בדיחה מהספר "מדריך הטרמפיסט לגלקסיה")
np.random.seed(42)

n_students = 50
n_subjects = 5

scores = np.random.normal(loc=80, scale=20, size=(n_students, n_subjects))
scores = np.clip(scores, 0, 100)

#general stats
print(np.mean(scores))
print(np.std(scores))
print(np.min(scores))
print(np.max(scores))

#average scores per subject and student
print(np.mean(scores, axis=0))
print(np.mean(scores, axis=1))

#top and bottom 5 students
student_averages = np.mean(scores, axis=1)
sorted_indices = np.argsort(student_averages)
top_5_indices = sorted_indices[-5:]
bottom_5_indices = sorted_indices[:5]

#student grades distribution
excellent = np.sum(student_averages >= 90)
good = np.sum((student_averages >= 80) & (student_averages < 90))
average = np.sum((student_averages >= 70) & (student_averages < 80))
struggling = np.sum(student_averages < 70)
print(f'Excellent: {excellent}, Good: {good}, Average: {average}, Struggling: {struggling}')

#finding outliers
def z_score_calculation(scores: np.ndarray) -> np.ndarray:
    mean = np.mean(scores , axis=0)
    std = np.std(scores , axis=0)
    return (scores - mean) / std
outliers = np.where(np.abs(z_score_calculation(scores)) > 2)[0]
print(f'Outliers: {outliers}')

#correlation matrix between subjects
correlation_matrix = np.corrcoef(scores.T)
print(correlation_matrix)

