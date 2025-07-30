import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/superbowl_rf_model.pkl")

# Load and prepare 2025 predicted data
data_2025 = pd.read_csv("data/predicted_2025_team_stats.csv")

teams = data_2025['Team']
X_2025 = data_2025.drop(columns=["Season", "Team", "Won_SB"])

# Predict
predictions = model.predict(X_2025)
probs = model.predict_proba(X_2025)[:, 1]  # probability of class 1 (winner)

# Attach results
data_2025["Predicted_Win"] = predictions
data_2025["Win_Probability"] = probs

# Show most likely winners
top_teams = data_2025.sort_values("Win_Probability", ascending=False)[["Team", "Win_Probability"]]
print("Top predicted Super Bowl contenders for 2025 season:")
print(top_teams.head(10))