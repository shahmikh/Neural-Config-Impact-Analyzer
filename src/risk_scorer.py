def calculate_risk_score(features):
    """
    Simple weighted risk scoring model
    Score range: 0 (safe) to 100 (critical)
    """

    score = 0

    # Weight choices are intentional and explainable
    score += features["num_nodes"] * 5
    score += features["num_edges"] * 10

    if features["has_wildcard_action"]:
        score += 40

    if features["has_wildcard_resource"]:
        score += 40

    return min(score, 100)


if __name__ == "__main__":
    # quick sanity test
    sample_features = {
        "num_nodes": 2,
        "num_edges": 1,
        "has_wildcard_action": 1,
        "has_wildcard_resource": 1
    }

    print("Risk Score:", calculate_risk_score(sample_features))

