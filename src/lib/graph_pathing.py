from shutil import Error
from igraph import Graph
from math import inf
from pprint import pprint


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
            if dist[u] + e["weight"] < dist[v]:
                dist[v] = dist[u] + e["weight"]
                prev[v] = e.source

    for e in graph.es:
        u = e.source
        v = e.target
        if dist[u] + e["weight"] < dist[v]:
            raise Error("Graph has negative weight cycle.")

    return (dist, prev)


class FloydWarshall:
    @staticmethod
    def distances_next_lists(graph: Graph) -> "tuple[list[list[int]], list[list[int]]]":
        total_vertices = len(graph.vs)

        distance = [[inf for _ in range(total_vertices)] for _ in range(total_vertices)]
        next_vertex = [[None for _ in range(total_vertices)] for _ in range(total_vertices)]

        for edge in graph.es:
            u = edge.source
            v = edge.target
            distance[u][v] = edge["weight"]
            next_vertex[u][v] = v

        for vertex in graph.vs:
            v = vertex.index
            distance[v][v] = 0
            next_vertex[v][v] = v

        for k in range(total_vertices):
            for i in range(total_vertices):
                for j in range(total_vertices):
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        next_vertex[i][j] = next_vertex[i][k]

        return (distance, next_vertex)

    @staticmethod
    def reconstruct_path(u: int, v: int, next_list: list[list[int]]) -> list[int]:
        if next_list[u][v] == None:
            return []

        path = [u]
        current_vertex = u

        while current_vertex != v:
            current_vertex = next_list[current_vertex][v]
            path.append(current_vertex)

        return path
