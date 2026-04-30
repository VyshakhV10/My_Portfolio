"""Reusable tools for chess game analytics."""

from chess_analytics.data import load_games, summarize_games, validate_games_columns
from chess_analytics.eda import (
    average_rating_diff_by_opening,
    average_rating_diff_by_victory_status,
    victory_status_counts,
    winner_counts,
)
from chess_analytics.features import (
    add_black_level,
    add_num_moves,
    add_rating_diff,
    add_white_level,
    build_features,
    rating_category,
    split_opening_name,
)
from chess_analytics.modeling import (
    encode_target,
    evaluate_classifier,
    prepare_features_and_target,
    split_train_test,
    train_random_forest,
    train_winner_model,
)
from chess_analytics.plots import plot_feature_importance

__all__ = [
    "add_black_level",
    "add_num_moves",
    "add_rating_diff",
    "add_white_level",
    "average_rating_diff_by_opening",
    "average_rating_diff_by_victory_status",
    "build_features",
    "encode_target",
    "evaluate_classifier",
    "load_games",
    "plot_feature_importance",
    "prepare_features_and_target",
    "rating_category",
    "split_opening_name",
    "split_train_test",
    "summarize_games",
    "train_random_forest",
    "train_winner_model",
    "validate_games_columns",
    "victory_status_counts",
    "winner_counts",
]
