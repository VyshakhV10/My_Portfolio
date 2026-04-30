import pandas as pd


def add_rating_diff(df: pd.DataFrame) -> pd.DataFrame:
    """Add the rating difference between white and black players."""
    df = df.copy()
    df["rating_diff"] = df["white_rating"] - df["black_rating"]
    return df


def add_num_moves(df: pd.DataFrame) -> pd.DataFrame:
    """Add the number of moves played in each game."""
    df = df.copy()
    df["num_moves"] = df["moves"].str.split().str.len()
    return df


def split_opening_name(df: pd.DataFrame) -> pd.DataFrame:
    """Split opening name into main opening and variation."""
    df = df.copy()
    opening_parts = df["opening_name"].str.split(":", n=1, expand=True)

    df["simple_opening"] = opening_parts[0]
    df["variation"] = opening_parts[1].fillna("Main line")

    return df


def rating_category(rating: int) -> str:
    """Convert a player rating into a broad skill level."""
    if rating < 1200:
        return "beginner"
    if rating < 1800:
        return "intermediate"
    return "advanced"


def add_white_level(df: pd.DataFrame) -> pd.DataFrame:
    """Add a broad skill level for the white player."""
    df = df.copy()
    df["white_level"] = df["white_rating"].apply(rating_category)
    return df


def add_black_level(df: pd.DataFrame) -> pd.DataFrame:
    """Add broad skill level for the black player."""
    df = df.copy()
    df["black_level"] = df["black_rating"].apply(rating_category)
    return df


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add all project features used for analysis and modeling."""
    df = add_rating_diff(df)
    df = add_num_moves(df)
    df = split_opening_name(df)
    df = add_white_level(df)
    df = add_black_level(df)
    return df
