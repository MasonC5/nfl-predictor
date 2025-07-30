import pandas as pd

# Load past seasons (e.g., 2022-2024) to derive trend
historical = pd.read_csv("data/engineered_team_stats.csv")
past_years = historical[historical["Season"].isin([2022, 2023, 2024])]

# Compute average performance for each team
grouped = past_years.groupby("Team").mean(numeric_only=True).reset_index()
grouped["Season"] = 2025  # Forecasting for next season

# Optionally adjust based on manual knowledge (injuries, draft, trades)
# e.g., grouped.loc[grouped["Team"] == "Kansas City Chiefs", "PF_off"] += 20

# Add placeholder Won_SB column for consistency with model input
grouped["Won_SB"] = 0

# Save predicted data
forecast_path = "data/predicted_2025_team_stats.csv"
grouped.to_csv(forecast_path, index=False)
print(f"✅ Saved 2025 forecasted team stats to: {forecast_path}")
