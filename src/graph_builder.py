import networkx as nx
from parser import load_iam_policy, extract_permissions


def build_permission_graph(permissions):
    """
    Builds a directed graph:
    action -> resource
    Nodes are namespaced to avoid collisions
    """

    G = nx.DiGraph()

    for action, resource in permissions:
        action_node = f"action:{action}"
        resource_node = f"resource:{resource}"

        G.add_node(action_node, type="action")
        G.add_node(resource_node, type="resource")
        G.add_edge(action_node, resource_node)

    return G


def calculate_blast_radius(graph):
    """
    Simple blast radius metrics
    """
    return graph.number_of_nodes(), graph.number_of_edges()


if __name__ == "__main__":
    policy = load_iam_policy("/home/shahmikh/neural-config-impact-analyzer/data/iam_policy_risky.json")
    permissions = extract_permissions(policy)

    graph = build_permission_graph(permissions)

    nodes, edges = calculate_blast_radius(graph)

    print("Nodes:")
    for n in graph.nodes(data=True):
        print(n)

    print("\nEdges:")
    for e in graph.edges():
        print(e)

    print("\nBlast Radius")
    print("Nodes:", nodes)
    print("Edges:", edges)

