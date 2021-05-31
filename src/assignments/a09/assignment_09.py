from igraph import Graph
from lib.graph_pathing import dijkstra


def assignment_09_1():
    print("9.1)")
    graph = Graph.TupleList(
        [
            ("u", "v", 2),
            ("u", "w", 5),
            ("u", "x", 1),
            ("v", "w", 3),
            ("v", "x", 2),
            ("w", "x", 3),
            ("w", "y", 1),
            ("w", "z", 5),
            ("x", "y", 1),
            ("y", "z", 2),
        ],
        vertex_name_attr="label",
        weights=True,
    )

    distances, _ = dijkstra(graph, graph.vs.find(label="w").index)
    print(f'Distances from "w": {distances}')


def assignment_09_2():
    print("9.2)")
    graph = Graph.TupleList(
        [
            ("A", "B", 5),
            ("A", "C", 7),
            ("A", "D", 1),
            ("B", "C", 2),
            ("C", "D", 6),
            ("C", "E", 5),
            ("D", "B", 3),
            ("D", "F", 5),
            ("D", "G", 3),
            ("E", "F", 4),
            ("F", "C", 1),
            ("G", "E", 1),
        ],
        vertex_name_attr="label",
        directed=True,
        weights=True,
    )

    for v in graph.vs:
        distances, _ = dijkstra(graph, v.index)
        print(f"Distances from \"{v['label']}\": {distances}")


def assignment_09_3():
    print("9.3)")
    vertex_label_map = { "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13 }
    graph_tuple_list = [
        ("a", "e", 5),
        ("a", "f", 1),
        ("a", "l", 2),
        ("b", "c", 11),
        ("b", "i", 9),
        ("c", "d", 3),
        ("c", "f", 3),
        ("c", "g", 5),
        ("c", "j", 6),
        ("d", "n", 5),
        ("e", "b", 1),
        ("e", "h", 8),
        ("f", "i", 6),
        ("f", "m", 4),
        ("g", "d", 4),
        ("g", "f", 1),
        ("h", "m", 7),
        ("i", "h", 10),
        ("j", "k", 13),
        ("j", "l", 8),
        ("m", "k", 9),
        ("n", "k", 6),
    ]

    graph_total_vertices = len(vertex_label_map.keys())
    graph_edges = [(vertex_label_map[t[0]], vertex_label_map[t[1]]) for t in graph_tuple_list]
    vertex_labels = list(vertex_label_map.keys())
    edge_weights = [t[2] for t in graph_tuple_list]

    graph = Graph(
        graph_total_vertices,
        edges=graph_edges,
        vertex_attrs={"label": vertex_labels},
        edge_attrs={"weight": edge_weights},
        directed=True,
    )

    for v in graph.vs:
        distances, _ = dijkstra(graph, v.index)
        print(f"Distances from \"{v['label']}\": {distances}")

def assignment_09():
    assignment_09_1()
    print()
    assignment_09_2()
    print()
    assignment_09_3()
