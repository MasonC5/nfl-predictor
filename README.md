# nfl-predictor

# 🏈 NFL Super Bowl Predictor (2025–2026)

Predict the Super Bowl champion using machine learning and historical NFL stats. 

## What is the goal?
To use team performance metrics from past NFL seasons to predict which team is most likely to win the Super Bowl in the 2025–2026 season.

---

## How we found this

- Data from Pro-Football-Reference and nflfastR
- Feature engineering: win %, point differential, turnovers, etc.
- Machine Learning models: Logistic Regression, Random Forest, XGBoost
- Model evaluation: accuracy, feature importance, ROC AUC

---

## Project Structure

nfl-predictor/
├── data/
│ ├── historical_team_stats.csv
│ └── engineered_team_stats.csv
├── notebooks/
│ ├── 01_explore_data.ipynb
│ └── 02_model_training.ipynb
├── scripts/
│ └── pfr_scraper.py
├── README.md
├── requirements.txt

