from igraph import Graph, plot
from lib.graph_utils import connected_components, subgraph
from lib.graph_search import depth_first_search_stack


def assignment_08():
    # graph = Graph(
    #     9,
    #     edges=[(0, 1), (1, 2), (1, 3), (4, 5), (6, 7), (6, 9), (7, 8), (8, 9)],
    #     vertex_attrs={"label": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
    # )

    labels  = [i for i in range(1, 13)]
    graph = Graph(12, vertex_attrs={"label": labels})
    graph.add_edges([(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 3), (3, 6), (3, 7), (4, 5), (4, 8), (4, 9), (5, 9), (6, 10), (6, 11)])

    depth_tree = Graph(
        len(graph.vs), vertex_attrs={"label": labels}# [i for i in range(len(graph.vs))]}
    )

    dfs_res = depth_first_search_stack(graph, 1, depth_tree=depth_tree, print_vertices=True)
    components = connected_components(graph)

    print(f"Vertices descobertos DFS: {dfs_res}")
    print(f"Total Componentes conexas: {len(components)}")
    for i, c in enumerate(components):
        print(c)
        g = subgraph(graph, c)
        plot(
            g,
            layout=g.layout('kk'),
            bbox=(800, 800),
            margin=50,
            vertex_label_dist=0,
            vertex_size=40,
            target=f"component_{i}.png"
        )

    plot(
        graph,
        layout=graph.layout("kk"),
        bbox=(800, 800),
        margin=50,
        vertex_label_dist=0,
        vertex_size=40,
        target="initial_graph.png",
    )

    remove_vertices = [
        v.index for v in depth_tree.vs if len(depth_tree.neighbors(v, mode="all")) == 0
    ]
    depth_tree.delete_vertices(remove_vertices)
   
    layout = depth_tree.layout('tree')
    # layout._coords.sort(key=lambda l: abs(l[0])+abs(l[1]))
    # vis = []
    # layout._coords[0][1] = 0.0
    # for v in depth_tree.vs:
    #     if v.index in vis:
    #         continue
    #     vis.append(v.index)
    #     for n in depth_tree.neighbors(v, mode='all'):
    #         if n not in vis:
    #             layout._coords[n][1] = layout._coords[v.index][1] + 0.5

    # print(layout._coords)

    plot(
        depth_tree,
        layout=layout,
        bbox=(800, 800),
        margin=50,
        vertex_label_dist=0,
        vertex_size=40,
        target="depth_tree.png"
    )


if __name__ == "__main__":
    assignment_08()