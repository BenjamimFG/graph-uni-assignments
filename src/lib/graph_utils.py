import matplotlib.pyplot as plt
from igraph import Graph
from math import inf
from .graph_search import depth_first_search_stack


def graph_from_incidence_matrix(inc_matrix):
    vertices = len(inc_matrix)
    edge_list = []

    for i in range(len(inc_matrix[0])):
        edge_vertices = []
        for j, arr in enumerate(inc_matrix):
            if arr[i] == 1:
                edge_vertices.append(j)

        edge_list.append(tuple(edge_vertices))

    return Graph(vertices, edge_list)


def plot_degree_histogram(degrees):
    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    plt.grid(True, linewidth=0.5, linestyle="dashed")

    ax = plt.hist(degrees, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], rwidth=0.95)

    plt.xticks([i for i in range(min(degrees) - 1, max(degrees) + 2)])
    plt.yticks([i for i in range(0, int(max(ax[0])) + 1)])

    plt.show()


def non_adjacent_vertices(graph: Graph) -> list:
    n = len(graph.vs)
    non_adjacent_vertices = []
    for i in range(n):
        for j in range(i + 1, n):
            if graph.get_eid(i, j, directed=False, error=False) == -1:
                non_adjacent_vertices.append((i, j))

    return non_adjacent_vertices


def graph_closure(graph: Graph) -> Graph:
    closure = graph.copy()
    n = len(closure.vs)
    vertices = non_adjacent_vertices(closure)

    for u, v in vertices:
        if closure.degree(u) + closure.degree(v) >= n:
            closure.add_edge(u, v)
            return graph_closure(closure)

    return closure


def is_full(graph: Graph) -> bool:
    n = len(graph.vs)
    for v in graph.vs:
        if v.degree() < n - 1:
            return False

    return True


def graph_diameter(distances_matrix: list) -> int:
    diameter = 0

    for cur_vertex_distances in distances_matrix:
        vertex_max_distance = max(cur_vertex_distances)
        if vertex_max_distance > diameter:
            diameter = vertex_max_distance

    return diameter


def graph_average_path_length(distances_matrix: list, vertex_count: int) -> float:
    distance_sum = 0
    distance_count = 0

    for i in range(vertex_count):
        for j in range(i + 1, vertex_count):
            distance_i_j = distances_matrix[i][j]
            distance_sum += distance_i_j if distance_i_j != inf else 0
            distance_count += 1

    return distance_sum / distance_count


def connected_components(graph: Graph):
    components = []
    visited = []

    for v in range(len(graph.vs)):
        if v not in visited:
            dfs_result = depth_first_search_stack(graph, v)
            components.append(dfs_result)
            visited.extend(dfs_result)

    components.sort(key=lambda l: len(l), reverse=True)

    return components


def subgraph(graph: Graph, vertices: "list[int]") -> Graph:
    new_graph = graph.copy()

    vertices_to_remove = [v.index for v in new_graph.vs if v.index not in vertices]
    new_graph.delete_vertices(vertices_to_remove)

    return new_graph
