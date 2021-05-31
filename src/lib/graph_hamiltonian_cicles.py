from igraph import Graph
from .graph_utils import non_adjacent_vertices, graph_closure, is_full


def dirac(graph: Graph) -> bool:
    n = len(graph.vs)
    if n < 3:
        return False

    for v in graph.vs:
        if v.degree() < n / 2:
            return False

    return True


def ore(graph: Graph) -> bool:
    n = len(graph.vs)
    vertices = non_adjacent_vertices(graph)

    for u, v in vertices:
        if graph.degree(u) + graph.degree(v) < n:
            return False

    return True


def bondy_and_chvatal(graph: Graph) -> bool:
    closure = graph_closure(graph)

    if is_full(closure):
        return True

    return False
