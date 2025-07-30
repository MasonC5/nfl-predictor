import pandas as pd
from pathlib import Path
from typing import Tuple

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"

OFFENSE_CANDIDATES = [
    DATA_DIR / "offense_historical_team_stats.csv",
]
DEFENSE_CANDIDATES = [
    DATA_DIR / "defense_historical_team_stats.csv",
]

def _resolve_path(candidates: list[Path]) -> Path:
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError("None of the candidate files were found: " + ", ".join(map(str, candidates)))

def load_historical_data(offense_path: Path | None = None, defense_path: Path | None = None) -> pd.DataFrame:
    if offense_path is None:
        offense_path = _resolve_path(OFFENSE_CANDIDATES)
    if defense_path is None:
        defense_path = _resolve_path(DEFENSE_CANDIDATES)

    off_df = pd.read_csv(offense_path, header=1)
    def_df = pd.read_csv(defense_path, header=1)

    off_df = off_df.rename(columns={"Year": "Season", "Tm": "Team"})
    def_df = def_df.rename(columns={"Year": "Season", "Tm": "Team"})

    off_df = off_df.add_suffix("_off")
    def_df = def_df.add_suffix("_def")

    off_df = off_df.rename(columns={"Season_off": "Season", "Team_off": "Team"})
    def_df = def_df.rename(columns={"Season_def": "Season", "Team_def": "Team"})

    merged = pd.merge(off_df, def_df, on=["Season", "Team"], how="inner")
    return merged

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df["Point_Diff"] = df["PF_off"] - df["PA_def"]
    df["Yard_Diff"] = df["Off_Yds_off"] - df["Def_Yds_def"]
    df["Turnover_Margin"] = df["Def_TO_def"] - df["Off_TO_off"]

    offense_cols = [col for col in df.columns if col.endswith("_off") and col not in {"Season", "Team"}]

    for col in offense_cols:
        base = col[:-4]  # remove '_off'
        def_col = base + "_def"
        diff_col = base.replace("Off_", "").replace("Def_", "") + "_Diff"
        if def_col in df.columns:
            df[diff_col] = df[col] - df[def_col]

    return df

def run() -> Tuple[int, int]:
    df = load_historical_data()
    df = engineer_features(df)
    output_path = DATA_DIR / "engineered_team_stats.csv"
    df.to_csv(output_path, index=False)
    rel_path = output_path.relative_to(ROOT_DIR)
    rows, cols = df.shape
    print(f"✅ Features added and saved to '{rel_path}' ({rows} rows, {cols} columns)")
    print(df.head().to_csv(index=False))
    return df.shape

if __name__ == "__main__":
    run()
