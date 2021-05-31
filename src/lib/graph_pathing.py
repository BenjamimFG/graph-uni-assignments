from shutil import Error
from igraph import Graph
from math import inf


def dijkstra(graph: Graph, origin_vertex: int) -> "tuple[list[int], list[int]]":
    vertex_set = set()

    dist = [inf] * len(graph.vs)
    prev = [None] * len(graph.vs)
    [vertex_set.add(v.index) for v in graph.vs]

    dist[origin_vertex] = 0

    while len(vertex_set) != 0:
        u = None
        for v in vertex_set:
            if u is None or dist[v] < dist[u]:
                u = v

        vertex_set.remove(u)

        for v in graph.neighbors(u, mode="out"):
            uv_eid = graph.get_eid(u, v)
            uv_edge = graph.es[uv_eid]
            alt = dist[u] + uv_edge["weight"]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return (dist, prev)


def bellman_ford(graph: Graph, origin_vertex: int) -> "tuple[list[int], list[int]]":  
    dist = [inf] * len(graph.vs)
    prev = [None] * len(graph.vs)

    dist[origin_vertex] = 0

    for _ in range(len(graph.vs)):
        for e in graph.es:
            u = e.source
            v = e.target
            if dist[u] + e['weight'] < dist[v]:
                dist[v] = dist[u] + e['weight']
                prev[v] = e.source
    
    for e in graph.es:
        u = e.source
        v = e.target
        if dist[u] + e['weight'] < dist[v]:
            raise Error("Grafo contém ciclo de peso negativo.")
    
    return (dist, prev)