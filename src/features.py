from parser import load_iam_policy, extract_permissions
from graph_builder import build_permission_graph


def extract_features(graph):
    """
    Converts graph into ML-ready security features
    """

    features = {}

    features["num_nodes"] = graph.number_of_nodes()
    features["num_edges"] = graph.number_of_edges()

    features["has_wildcard_action"] = 0
    features["has_wildcard_resource"] = 0

    for node, data in graph.nodes(data=True):
        if data.get("type") == "action" and node.endswith(":*"):
            features["has_wildcard_action"] = 1

        if data.get("type") == "resource" and node.endswith(":*"):
            features["has_wildcard_resource"] = 1

    return features


if __name__ == "__main__":
    policy = load_iam_policy("/home/shahmikh/neural-config-impact-analyzer/data/iam_policy_risky.json")
    permissions = extract_permissions(policy)

    graph = build_permission_graph(permissions)

    features = extract_features(graph)

    print("Extracted Features:")
    for k, v in features.items():
        print(f"{k}: {v}")

