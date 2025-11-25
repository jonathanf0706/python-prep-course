import json
import pandas as pd

# --- שלב 1: טעינת ה-JSON מהקובץ ---
# אנו קוראים את קובץ ה-JSON המקונן מהדיסק.
# json.load קורא את הקובץ והופך אותו למילון (dict) בפייתון.
with open("python-prep-course/day06/datasets/spotify_nested_large.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# --- שלב 2: חילוץ רשימת ה-tracks מתוך המילון ---
# data מכיל מפתח בשם "tracks" שמחזיק רשימה של שירים.
tracks = data["tracks"]

# --- שלב 3: הפיכת המבנה המקונן לטבלה "שטוחה" ---
# json_normalize לוקח רשימת מילונים ומפרק שדות מקוננים לעמודות.
flat_df = pd.json_normalize(tracks)

print("Before Cleaning:\n", flat_df.head(), "\n")

# --- שלב 4: יצירת עמודת Missing Flag ---
# אנו מסמנים אילו ערכים בעמודת השנה היו חסרים (NaN) לפני הניקוי.
flat_df["album_year_missing"] = flat_df["album.year"].isna()

# --- שלב 5: מילוי album.year באופן מקצועי ---
# median (חציון) נבחר כי הוא לא מושפע מערכים קיצוניים.
median_year = flat_df["album.year"].median()
flat_df["album.year"] = flat_df["album.year"].fillna(median_year)

# --- שלב 6: ניקוי album.title ---
# מילוי טקסט חסר בערך ברירת מחדל שאינו מפריע לניתוחים.
flat_df["album.title"] = flat_df["album.title"].fillna("Unknown Album")

# --- שלב 7: ניקוי features (danceability & energy) ---
# ממלאים NaN לפי הממוצע של כל עמודה.
flat_df["features.danceability"] = flat_df["features.danceability"].fillna(
    flat_df["features.danceability"].mean()
)
flat_df["features.energy"] = flat_df["features.energy"].fillna(
    flat_df["features.energy"].mean()
)

# --- שלב 8: ניקוי name ---
# שם שיר חסר → נותנים ערך ברירת מחדל "Unknown Song".
flat_df["name"] = flat_df["name"].fillna("Unknown Song")

# --- שלב 9: בדיקה סופית של חוסרים ---
print("Missing Values After Cleaning:\n", flat_df.isna().sum(), "\n")

# --- שלב 10: הדפסת הטבלה לאחר הניקוי ---
print("After Cleaning:\n", flat_df.head(), "\n")

# --- שלב 11: שמירת קובץ CSV לשימוש בהמשך ו-commit ---
# שמירה לקובץ נקי לעבודה בהמשך.
flat_df.to_csv("clean_spotify_dataset.csv", index=False)

print("Saved clean_spotify_dataset.csv successfully!")