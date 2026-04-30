import matplotlib.pyplot as plt
import pandas as pd


def plot_feature_importance(model, feature_names: list[str] | pd.Index):
    """Plot feature importance values from a trained model."""
    fig, ax = plt.subplots()

    ax.bar(feature_names, model.feature_importances_)
    ax.set_title("Feature Importance")
    ax.set_xlabel("Feature")
    ax.set_ylabel("Importance")

    return fig, ax
