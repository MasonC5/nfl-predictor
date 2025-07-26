import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import time

def clean(df):
    df = df[df['Team'] != 'League Total']
    df['Team'] = df['Team'].str.replace("*", "", regex=False)
    return df

def scrape_year(year):
    url = f'https://www.pro-football-reference.com/years/{year}/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    offense_table = soup.find('table', id='team_stats')
    defense_table = soup.find('table', id='opponents')

    if offense_table and defense_table:
        off = pd.read_html(str(offense_table))[0]
        defn = pd.read_html(str(defense_table))[0]

        off = clean(off)
        defn = clean(defn)

        off['Year'] = year
        defn['Year'] = year

        df = pd.merge(off, defn, on=['Team', 'Year'], suffixes=('_off', '_def'))
        return df
    else:
        return None

def run_scraper(start=2000, end=2024):
    all_years = []
    for year in range(start, end + 1):
        print(f"Scraping {year}...")
        data = scrape_year(year)
        if data is not None:
            all_years.append(data)
        time.sleep(1.5)

    final_df = pd.concat(all_years)
    os.makedirs('data', exist_ok=True)
    final_df.to_csv('data/historical_team_stats.csv', index=False)
    print("✅ Data saved to 'data/historical_team_stats.csv'")

if __name__ == "__main__":
    run_scraper()