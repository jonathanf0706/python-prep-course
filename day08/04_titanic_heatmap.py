import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("../day06/datasets/train.csv")
print(df.head())
print(df.dtypes)

numeric_df = df[["PassengerId", "Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]]

corr_matrix = numeric_df.corr()
print(corr_matrix)


plt.figure(figsize=(10, 6))        # גודל הגרף
sns.heatmap(
    corr_matrix,
    annot=True,                    # כותב את הערכים בתוך התאים
    cmap="coolwarm",               # צבעים (כחול = שלילי, אדום = חיובי)
    linewidths=0.5,                # קווי הפרדה בין התאים
    fmt=".2f"                      # הצגת המספרים עם 2 ספרות אחרי הנקודה
)
plt.title("Titanic Correlation Heatmap")
plt.tight_layout()

plt.savefig("../outputs/titanic_heatmap.png")
plt.show()
