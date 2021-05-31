from igraph import Graph, plot
from lib.graph_search import depth_first_search


def assignment_07():
    # graph = Graph(
    #     8,
    #     edges=[
    #         (0, 2),
    #         (0, 3),
    #         (1, 2),
    #         (1, 3),
    #         (2, 3),
    #         (2, 7),
    #         (3, 5),
    #         (3, 6),
    #         (4, 5),
    #         (4, 6),
    #         (5, 6),
    #     ],
    #     vertex_attrs={"label": [1, 2, 3, 4, 5, 6, 7, 8]},
    # )

    labels  = [i for i in range(1, 13)]
    graph = Graph(12, vertex_attrs={"label": labels})
    graph.add_edges([(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 3), (3, 6), (3, 7), (4, 5), (4, 8), (4, 9), (5, 9), (6, 10), (6, 11)])

    depth_tree = Graph(12, vertex_attrs={"label": labels}) #[1, 2, 3, 4, 5, 6, 7, 8]})
    depth_first_search(graph, 1, print_vertices=True, depth_tree=depth_tree)

    plot(
        graph,
        layout=graph.layout("kk"),
        bbox=(800, 800),
        margin=50,
        vertex_label_dist=0,
        vertex_size=40,
        target="initial_graph.png",
    )
    plot(
        depth_tree,
        layout=depth_tree.layout("tree"),
        bbox=(1600, 1600),
        margin=50,
        vertex_label_dist=0,
        vertex_size=40,
        target="depth_tree.png",
    )


if __name__ == "__main__":
    assignment_07()