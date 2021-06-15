from igraph import Graph
from lib.graph_flow import ford_fulkerson


def assignment_12():
    graph = Graph.TupleList(
        [
            ("A", "B", 16),
            ("A", "C", 13),
            ("B", "C", 10),
            ("B", "D", 12),
            ("C", "B",  4),
            ("C", "E", 14),
            ("D", "C",  9),
            ("D", "F", 20),
            ("E", "D",  7),
            ("E", "F",  4)
        ],
        vertex_name_attr="label",
        directed=True,
        weights=True,
    )

    print("Fluxo Máximo: " + str( ford_fulkerson(graph, 1, 5, print_each_iter=True) ))