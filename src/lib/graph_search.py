from igraph import Graph
from math import inf
from queue import Queue


def depth_first_search(
    graph: Graph,
    initial_vertex: int,
    discovered: list = [],
    print_vertices=False,
    depth_tree: Graph = None,
):
    discovered.append(initial_vertex)

    if print_vertices:
        print(initial_vertex + 1)

    for w in graph.neighbors(initial_vertex, mode="all"):
        if w not in discovered:
            if depth_tree is not None:
                depth_tree.add_edge(initial_vertex, w)

            depth_first_search(
                graph,
                w,
                discovered=discovered,
                print_vertices=print_vertices,
                depth_tree=depth_tree,
            )


def depth_first_search_stack(
    graph: Graph,
    initial_vertex: int,
    print_vertices=False,
    depth_tree: Graph = None,
):
    discovered = []
    stack = [initial_vertex]
    last = -1

    while len(stack) > 0:
        u = stack.pop()
        if u not in discovered:
            if print_vertices:
                print(u)
            if depth_tree is not None and last >= 0:
                depth_tree.add_edge(last, u)
            discovered.append(u)
            last = u
            for v in graph.neighbors(u, mode="all"):
                stack.append(v)

    return discovered


def breadth_first_search(graph: Graph, origin: int, print_queue=False):
    total_vertices = graph.vcount()
    color = ["WHITE"] * total_vertices
    parent = [None] * total_vertices
    distance = [inf] * total_vertices

    color[origin] = "GRAY"
    distance[origin] = 0

    Q = Queue()
    Q.put(origin)

    while Q.qsize() != 0:
        if print_queue:
            print(list(Q.queue))
        u = Q.get()
        for v in graph.neighbors(u, mode="out"):
            if color[v] == "WHITE":
                color[v] = "GRAY"
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)
        color[u] = "BLACK"

    return (color, parent, distance)


def bfs_generator_tree(graph: Graph, origin: int) -> Graph:
    total_vertices = graph.vcount()
    generator_tree = Graph(total_vertices)
    color = ["WHITE"] * total_vertices
    parent = [None] * total_vertices
    distance = [inf] * total_vertices

    color[origin] = "GRAY"
    distance[origin] = 0

    Q = Queue()
    Q.put(origin)

    while Q.qsize() != 0:
        u = Q.get()
        for v in graph.neighbors(u, mode="out"):
            if color[v] == "WHITE":
                generator_tree.add_edge(u, v)
                color[v] = "GRAY"
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)
        color[u] = "BLACK"

    return generator_tree
