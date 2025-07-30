# 🏈 NFL Super Bowl Predictor

This project uses machine learning to predict NFL Super Bowl winners based on historical team performance metrics, and how these winners have scored statistically over time. It combines offensive and defensive stats, feature engineering, model training, and future forecasting for predictive insights.

---

# Current Top 5 Contenders Using my Predicted Stats



```

## Structure

nfl-predictor/
├── data/
│   ├── offense_historical_team_stats.csv
│   ├── defense_historical_team_stats.csv
│   ├── engineered_team_stats.csv
│   └── predicted_2025_team_stats.csv
├── models/
│   └── superbowl_rf_model.pkl
├── notebooks/
│   ├── 01_explore_data.ipynb
│   └── 02_model_training.ipynb
├── scripts/
│   ├── feature_engineering.py
│   ├── forecast_2025_stats.py
│   ├── train_model.py
│   └── predict_2025_winner.py
├── requirements.txt
└── README.md
```

---

## Setup the project

1. Clone repository:

   ```bash
   git clone https://github.com/yourusername/nfl-predictor.git
   cd nfl-predictor
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   pip install imbalanced-learn
   ```

---

## Order of info

### 1. Feature Engineering

```bash
python scripts/feature_engineering.py
```

Generates engineered stats from historical offense and defense data.

### 2. Forecast 2025 Stats

```bash
python scripts/forecast_2025_stats.py
```

Creates a projected 2025 dataset based on recent seasons.

### 3. Model Training

```bash
python scripts/train_model.py
```

Trains and saves a Random Forest model using SMOTE to balance Super Bowl winners.

### 4. Predict 2025 Winner

```bash
python scripts/predict_2025_winner.py
```

This will print the top predicted teams most likely to win the 2025 Super Bowl.

---

## Notebooks

* `01_explore_data.ipynb`: Explore trends, correlations, and feature distributions.
* `02_model_training.ipynb`: Experiment with modeling, tuning, and evaluation.

---

## My Current/Future Work

* Start 'Em/Sit 'Em (In Progress)
---

## 📄 License

You can find the licensing file in this folder.
