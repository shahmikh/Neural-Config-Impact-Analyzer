import json

def load_iam_policy(path):
    with open(path, "r") as f:
        policy = json.load(f)
    return policy

def extract_permissions(policy):
    permissions = []

    for stmt in policy.get("Statement", []):
        actions = stmt.get("Action", [])
        resources = stmt.get("Resource", [])

        if isinstance(actions, str):
            actions = [actions]
        if isinstance(resources, str):
            resources = [resources]

        for action in actions:
            for resource in resources:
                permissions.append((action, resource))

    return permissions


if __name__ == "__main__":
    policy = load_iam_policy("/home/shahmikh/neural-config-impact-analyzer/data/iam_policy_risky.json")
    perms = extract_permissions(policy)

    for p in perms:
        print(p)

