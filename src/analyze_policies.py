from parser import load_iam_policy, extract_permissions
from graph_builder import build_permission_graph, calculate_blast_radius
from features import extract_features
from risk_scorer import calculate_risk_score
from explainer import explain_risk
from predictor import predict_risk
from remediator import suggest_safer_policy
import json
import os



POLICIES = {
    "safe": "data/iam_policy_safe.json",
    "medium": "data/iam_policy_medium.json",
    "risky": "data/iam_policy_risky.json"
}


def analyze_policy(name, path):
    policy = load_iam_policy(path)
    permissions = extract_permissions(policy)
    graph = build_permission_graph(permissions)

    nodes, edges = calculate_blast_radius(graph)
    features = extract_features(graph)
    risk_score = calculate_risk_score(features)
    ml_risk = predict_risk(features)
    safer_policy = suggest_safer_policy(policy)
    os.makedirs("output", exist_ok=True)
    output_path = f"output/{name}_safer_policy.json"

    with open(output_path, "w") as f:
        json.dump(safer_policy, f, indent=2)



    explanation = explain_risk(features)

    return {
        "policy": name,
        "blast_radius_nodes": nodes,
        "blast_radius_edges": edges,
        "risk_score": risk_score,
        "ml_risk": ml_risk,
        "explanation": explanation,
        "safer_policy": safer_policy,
        "output_path": output_path,
        "features": features
    }


if __name__ == "__main__":
    for name, path in POLICIES.items():
        result = analyze_policy(name, path)

        print("\nPolicy:", result["policy"])
        print("Blast Radius:", result["blast_radius_nodes"], "nodes,", result["blast_radius_edges"], "edges")
        print("Risk Score:", result["risk_score"])
        print("ML Predicted Risk Level:", result["ml_risk"])
        print("Explanation:")
        for r in result["explanation"]:
            print(" -", r)

        print("Features:")
        

        for k, v in result["features"].items():
            print(f"  {k}: {v}")
     #   print("Suggested Safer Policy:")
    #    print(result["safer_policy"])
        print("Suggested Safer Policy saved to:", result["output_path"])



