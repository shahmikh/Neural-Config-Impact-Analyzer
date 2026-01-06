def suggest_safer_policy(policy):
    """
    Generates a safer version of an IAM policy
    by removing wildcards
    """

    safer_policy = policy.copy()
    safer_policy["Statement"] = []

    for stmt in policy.get("Statement", []):
        new_stmt = stmt.copy()

        actions = stmt.get("Action", [])
        resources = stmt.get("Resource", [])

        if actions == "*" or "*" in actions:
            new_stmt["Action"] = ["s3:GetObject"]

        if resources == "*" or "*" in resources:
            new_stmt["Resource"] = ["arn:aws:s3:::example-bucket/*"]

        safer_policy["Statement"].append(new_stmt)

    return safer_policy


if __name__ == "__main__":
    import json

    risky_policy = {
        "Statement": [
            {"Effect": "Allow", "Action": "*", "Resource": "*"}
        ]
    }

    print(json.dumps(suggest_safer_policy(risky_policy), indent=2))

