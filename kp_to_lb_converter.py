import json
import re
import pandas as pd

from datetime import datetime


with open('kp_ratings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

entries = []
for entry in data:
    alt = entry["alt"]
    match = re.match(r'(.*)\s\((\d{4})\)', alt)

    if match:
        title = match.group(1).strip()
        year = match.group(2)
    else:
        title = alt
        year = ""

    date = datetime.strptime(entry["time"], '%d.%m.%y %H:%M')
    watched_date = f"{date:%Y-%m-%d}"
    entries.append({
        "Title": title.strip(),
        "Year": year,
        "Rating10": entry["value"],
        "WatchedDate": watched_date, 
        "IsFilm": "film" in entry['url'],
    })

df = pd.DataFrame(entries, columns=['Title', 'Year', 'Rating10', 'WatchedDate', 'IsFilm'])
print(f"Total entries: {len(df)}\nFilms count: {len(df[df['IsFilm']])}\nSeries count: {len(df[~df['IsFilm']])}")
print("Dates range: ", df['WatchedDate'].min(), df['WatchedDate'].max())
print("Ratings range: ", df['Rating10'].min(), df['Rating10'].max())
print("Sample data:\n", df.head(), sep='')

df[df['IsFilm']].to_csv('films_rating.csv', index=False, columns=['Title', 'Year', 'Rating10', 'WatchedDate'])
df[~df['IsFilm']].to_csv('series_rating.csv', index=False, columns=['Title', 'Year', 'Rating10', 'WatchedDate'])
