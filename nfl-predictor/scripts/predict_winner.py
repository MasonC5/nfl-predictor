import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load model (if you save it with joblib)
# model = joblib.load('models/sb_model.pkl')

# OR retrain it quickly here
df = pd.read_csv('data/engineered_team_stats.csv')
df['Won_SB'] = df['Team'].apply(lambda x: 1 if x in ['New England Patriots', 'Kansas City Chiefs'] else 0)
X = df[['Point_Diff', 'Yard_Diff', 'Turnover_Margin']]
y = df['Won_SB']
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 2025 example data input (replace with real later)
example_team = pd.DataFrame([{
    'Point_Diff': 120,
    'Yard_Diff': 500,
    'Turnover_Margin': 5
}])

prediction = model.predict(example team)
print("This team is likely to win the Super Bowl!" if prediction[0] == 1 else "❌ This team is unlikely to win.")
