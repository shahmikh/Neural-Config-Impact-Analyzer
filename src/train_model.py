import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib


def train():
    df = pd.read_csv("data/training_data.csv")

    X = df.drop("risk_label", axis=1)
    y = df["risk_label"]

    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X, y)

    joblib.dump(model, "models/risk_model.pkl")
    print("Model trained and saved.")


if __name__ == "__main__":
    train()

