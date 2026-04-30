from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "id",
    "rated",
    "created_at",
    "last_move_at",
    "turns",
    "victory_status",
    "winner",
    "increment_code",
    "white_id",
    "white_rating",
    "black_id",
    "black_rating",
    "moves",
    "opening_eco",
    "opening_name",
    "opening_ply",
]


def load_games(path: str | Path) -> pd.DataFrame:
    """Load the chess games dataset."""
    return pd.read_csv(path)


def validate_games_columns(df: pd.DataFrame) -> None:
    """Check that the dataset contains the columns used by this project."""
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")


def summarize_games(df: pd.DataFrame) -> dict:
    """Return basic summary information about the games dataset."""
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": df.isna().sum().to_dict(),
    }
