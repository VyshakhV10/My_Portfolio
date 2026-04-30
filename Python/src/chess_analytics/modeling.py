import pandas as pd
from numpy.typing import NDArray
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def prepare_features_and_target(
    df: pd.DataFrame,
    feature_columns: list[str] | None = None,
    target_column: str = "winner",
) -> tuple[pd.DataFrame, pd.Series]:
    """Split the dataset into model features and target."""
    if feature_columns is None:
        feature_columns = ["rating_diff", "num_moves"]

    x = df[feature_columns]
    y = df[target_column]
    return x, y


def encode_target(y: pd.Series) -> tuple[NDArray, LabelEncoder]:
    """Encode text target labels as numbers for machine learning."""
    encoder = LabelEncoder()
    encoded_y = encoder.fit_transform(y)
    return encoded_y, encoder


def split_train_test(
    x: pd.DataFrame,
    y: pd.Series | NDArray,
    test_size: float = 0.2,
    random_state: int = 42,
):
    """Create train and test datasets."""
    return train_test_split(x, y, test_size=test_size, random_state=random_state)


def train_random_forest(
    x_train: pd.DataFrame,
    y_train: pd.Series,
    random_state: int = 42,
) -> RandomForestClassifier:
    """Train a Random Forest classifier."""
    model = RandomForestClassifier(random_state=random_state)
    model.fit(x_train, y_train)
    return model


def evaluate_classifier(model, x_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """Return accuracy, predictions, and classification report for a classifier."""
    y_pred = model.predict(x_test)

    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "classification_report": classification_report(y_test, y_pred),
        "predictions": y_pred,
    }


def train_winner_model(
    df: pd.DataFrame,
    feature_columns: list[str] | None = None,
    test_size: float = 0.2,
    random_state: int = 42,
) -> dict:
    """Train and evaluate the winner prediction model used in the notebook."""
    x, y = prepare_features_and_target(df, feature_columns, target_column="winner")
    encoded_y, encoder = encode_target(y)
    x_train, x_test, y_train, y_test = split_train_test(
        x,
        encoded_y,
        test_size=test_size,
        random_state=random_state,
    )
    model = train_random_forest(x_train, y_train, random_state=random_state)
    evaluation = evaluate_classifier(model, x_test, y_test)

    return {
        "model": model,
        "encoder": encoder,
        "features": x,
        "x_train": x_train,
        "x_test": x_test,
        "y_train": y_train,
        "y_test": y_test,
        **evaluation,
    }
