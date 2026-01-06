def explain_risk(features):
    """
    Converts technical risk signals into human-readable explanations
    """

    reasons = []

    if features["has_wildcard_action"]:
        reasons.append(
            "Policy allows all actions (*), which enables unrestricted operations."
        )

    if features["has_wildcard_resource"]:
        reasons.append(
            "Policy applies to all resources (*), increasing blast radius."
        )

    if features["num_edges"] > 1:
        reasons.append(
            "Multiple permission relationships increase access complexity."
        )

    if features["num_nodes"] > 2:
        reasons.append(
            "Large number of permission entities expands attack surface."
        )

    if not reasons:
        reasons.append(
            "Policy follows least-privilege principles with limited scope."
        )

    return reasons


if __name__ == "__main__":
    sample_features = {
        "num_nodes": 2,
        "num_edges": 1,
        "has_wildcard_action": 1,
        "has_wildcard_resource": 1
    }

    for r in explain_risk(sample_features):
        print("-", r)

