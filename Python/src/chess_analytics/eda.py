import pandas as pd


def average_rating_diff_by_opening(df: pd.DataFrame) -> pd.Series:
    """Calculate average rating difference for each opening."""
    return df.groupby("simple_opening")["rating_diff"].mean().sort_values(ascending=False)


def average_rating_diff_by_victory_status(df: pd.DataFrame) -> pd.Series:
    """Calculate average rating difference for each victory status."""
    return df.groupby("victory_status")["rating_diff"].mean().sort_values(ascending=False)


def winner_counts(df: pd.DataFrame) -> pd.Series:
    """Count how often each winner label appears."""
    return df["winner"].value_counts()


def victory_status_counts(df: pd.DataFrame) -> pd.Series:
    """Count how often each victory status appears."""
    return df["victory_status"].value_counts()
