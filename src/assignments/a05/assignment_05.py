import igraph
from lib.graph_search import breadth_first_search


def assignment_05():
    graph = igraph.Graph(8)
    graph.add_edges([(0, 4), (0,1), (1, 5), (2, 3), (2, 5), (2, 6), (3, 6), (3, 7), (5, 6), (6, 7)])

    _, s_parent, s_distance = breadth_first_search(graph, 1)

    print('Origin s:')
    print(f'¶ = {s_parent}')
    print(f'd = {s_distance}')

    print('\nOrigin t:')
    breadth_first_search(graph, 2, print_queue=True)

    print('\nOrigin x:')
    breadth_first_search(graph, 6, print_queue=True)


if __name__ == '__main__':
    assignment_05()