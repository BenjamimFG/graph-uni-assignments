from igraph import Graph
from lib.graph_pathing import bellman_ford

def assignment_10_1():
    print("10.1)")
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

    # for v in graph.vs:
    #     distances, _ = bellman_ford(graph, v.index)
    #     print(f"Distances from \"{v['label']}\": {distances}")
    
    v = graph.vs.select(label="A")[0]

    distances, parent = bellman_ford(graph, v.index)
    # print(f"Distances from \"{v['label']}\": {distances}")
    parent_labels = []
    for p in parent:
        if p:
            parent_labels.append(graph.vs[p]['label'])
        else:
            parent_labels.append(p)
    # print(f"Parents from \"{v['label']}\": {parent_labels}")

    for i in range(len(distances)):
        print(f"Distance from {v['label']} to {graph.vs[i]['label']}: {distances[i]} | Previous: {parent_labels[i]}")


def assignment_10_2():
    print("10.2)")
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

    v = graph.vs.select(label="a")[0]

    distances, parent = bellman_ford(graph, v.index)
    parent_labels = []
    for p in parent:
        if p:
            parent_labels.append(graph.vs[p]['label'])
        else:
            parent_labels.append(p)

    for i in range(len(distances)):
        print(f"Distance from {v['label']} to {graph.vs[i]['label']}: {str(distances[i]).ljust(3)} | Previous: {parent_labels[i]}")



def assignment_10():
    assignment_10_1()
    print()
    assignment_10_2()