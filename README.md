# nfl-predictor

# 🏈 NFL Super Bowl Predictor (2025–2026)

Predict the Super Bowl champion using machine learning and historical NFL stats.

## 🎯 Goal
Use team performance metrics from past NFL seasons to predict which team is most likely to win the Super Bowl in the 2025–2026 season.

---

## 🧠 What’s Inside

- Data from Pro-Football-Reference and nflfastR
- Feature engineering: win %, point differential, turnovers, etc.
- Machine Learning models: Logistic Regression, Random Forest, XGBoost
- Model evaluation: accuracy, feature importance, ROC AUC

---

## 📁 Project Structure

nfl-superbowl-predictor/
├── data-import/
│   └── historical_team_stats.csv         # Output of scraper
├── notebooks/
│   └── 01_data_cleaning.ipynb
│   └── 02_model_training.ipynb
├── scripts/
│   └── pfr_scraper.py                    # Scraper script
├── predictor.py                          # Final model script
├── requirements.txt
├── README.md

