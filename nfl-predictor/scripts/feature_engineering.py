import pandas as pd
import os

def engineer_features(df):
    df['Point_Diff'] = df['PF_off'] - df['PA_def']
    df['Yard_Diff'] = df['Yds_off'] - df['Yds_def']
    df['Turnover_Margin'] = df['TO_def'] - df['TO_off']
    return df

def run():
    df = pd.read_csv('data/historical_team_stats.csv')
    df = engineer_features(df)
    df.to_csv('data/engineered_team_stats.csv', index=False)
    print("✅ Features added and saved to 'data/engineered_team_stats.csv'")

if __name__ == '__main__':
    run()
