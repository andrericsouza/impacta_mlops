import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split

def load_diamonds():
    """Carrega o dataset de diamantes do seaborn."""
    df = sns.load_dataset("diamonds")
    return df


def split_features_target(df: pd.DataFrame):
    """Separa X e y."""
    y = df["price"]
    X = df.drop(columns=["price"])
    return X, y


def train_test_split_diamonds(test_size: float = 0.2, random_state: int = 42):
    """Carrega, separa e faz o split em treino e teste."""
    df = load_diamonds()
    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test
