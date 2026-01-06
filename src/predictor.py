import joblib
import pandas as pd


MODEL_PATH = "models/risk_model.pkl"


def predict_risk(features):
    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]

    return prediction


if __name__ == "__main__":
    sample_features = {
        "num_nodes": 2,
        "num_edges": 1,
        "has_wildcard_action": 1,
        "has_wildcard_resource": 1
    }

    risk = predict_risk(sample_features)
    print("Predicted risk level:", risk)

