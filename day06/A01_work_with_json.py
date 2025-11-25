import pandas as pd
import json

with open("python-prep-course/day06/datasets/spotify_nested_large.json", "r", encoding="utf-8") as f:
    data = json.load(f)

tracks = data["tracks"]
# print(tracks)
df = pd.DataFrame(tracks)
print(df)
flat_df = pd.json_normalize(tracks)
print(flat_df)
print(flat_df.isna().sum())
