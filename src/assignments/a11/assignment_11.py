from igraph import Graph
from lib.graph_pathing import FloydWarshall


def assignment_11():
    graph = Graph.TupleList(
        [
            ("1", "2", 3),
            ("1", "3", 8),
            ("2", "4", 1),
            ("2", "5", 7),
            ("1", "5", -4),
            ("3", "2", 4),
            ("4", "3", -5),
            ("4", "1", 2),
            ("5", "4", 6),
        ],
        vertex_name_attr="label",
        directed=True,
        weights=True,
    )

    distances, next_vertex = FloydWarshall.distances_next_lists(graph)

    print("╔" + "═" * 10 + "╦" + "═" * 10 + "╦" + "═" * 10 + "╦" + "═" * 18 + "╗")
    print("║  Source  ║  Target  ║ Distance ║       Path       ║")
    for u in graph.vs:
        print("╠" + "═" * 10 + "╬" + "═" * 10 + "╬" + "═" * 10 + "╬" + "═" * 18 + "╣")
        for v in graph.vs:
            u_label = u["label"].center(10)
            v_label = v["label"].center(10)
            dist_str = str(distances[u.index][v.index]).center(10)
            path = FloydWarshall.reconstruct_path(u.index, v.index, next_vertex)
            path = list(map(lambda x: x + 1, path))
            path_str = str(path).center(18)
            print(
                f'║{u_label}║{v_label}║{dist_str}║{path_str}║'
            )
            print(
                "╠" + "═" * 10 + "╬" + "═" * 10 + "╬" + "═" * 10 + "╬" + "═" * 18 + "╣"
            )

        print("║" + " " * 10 + "║" + " " * 10 + "║" + " " * 10 + "║" + " " * 18 + "║")

    print("╚" + "═" * 10 + "╩" + "═" * 10 + "╩" + "═" * 10 + "╩" + "═" * 18 + "╝")
