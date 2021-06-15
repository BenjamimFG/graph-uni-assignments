from igraph import Graph
from .graph_pathing import bellman_ford
from math import inf


def ford_fulkerson(
    graph: Graph, source: int, target: int, print_each_iter=False) -> int:
    max_flow = 0
    residual_graph = graph.copy()

    i = 0
    while True:
        dist, vertices_parents = bellman_ford(residual_graph, source, check_negative_weight_cycle=False)
        if dist[target] == inf:
            break

        current_flow = inf
        v = target
        while v != source:
            u = vertices_parents[v]
            edge_u_v_id = residual_graph.get_eid(u, v, directed=True, error=False)
            if edge_u_v_id != -1:
                edge_u_v = residual_graph.es[edge_u_v_id]
                current_flow = min(current_flow, edge_u_v["weight"])
            v = vertices_parents[v]

        v = target
        while v != source:
            u = vertices_parents[v]
            edge_u_v_id = residual_graph.get_eid(u, v, directed=True, error=False)
            if edge_u_v_id != -1:
                edge_u_v = residual_graph.es[edge_u_v_id]
                edge_u_v["weight"] -= current_flow

            edge_v_u_id = residual_graph.get_eid(v, u, directed=True, error=False)
            if edge_v_u_id != -1:
                edge_v_u = residual_graph.es[edge_v_u_id]
                edge_v_u["weight"] += current_flow
            v = vertices_parents[v]

        max_flow += current_flow
        if print_each_iter:
            print(f'----------- {i+1}ª iteração -----------')
            print(f"Fluxo Máximo: {max_flow}")
            residual_network = [
                (
                    residual_graph.vs[e.source]["label"],
                    residual_graph.vs[e.target]["label"],
                    e["weight"],
                )
                for e in residual_graph.es
            ]
            print("Rede Residual: [")
            for rn in residual_network:
                print(f"\t{rn},")
            print("]\n")
            i += 1

    return max_flow
