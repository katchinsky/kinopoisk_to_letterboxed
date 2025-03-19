import json
import re
import requests
import pandas as pd
import click

from datetime import datetime

@click.command()
@click.argument('user_id', type=int)
def main(user_id):
    url = f'https://www.kinopoisk.ru/graph_data/last_vote_data/{user_id % 1000}/last_vote_{user_id}__all.json'

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    raw_text = response.text
    data = json.loads(raw_text[raw_text.find('['):raw_text.rfind(']') + 1])

    entries = []
    with click.progressbar(data) as bar:

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

    df[df['IsFilm']].to_csv(f'{user_id}_films_rating.csv', index=False, columns=['Title', 'Year', 'Rating10', 'WatchedDate'])
    df[~df['IsFilm']].to_csv(f'{user_id}_series_rating.csv', index=False, columns=['Title', 'Year', 'Rating10', 'WatchedDate'])

if __name__ == '__main__':
    main()