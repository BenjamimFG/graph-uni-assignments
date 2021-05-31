import igraph
from lib.graph_search import breadth_first_search, bfs_generator_tree
from lib.graph_utils import graph_diameter, graph_average_path_length


def generating_tree():
    graph = igraph.Graph(8)
    graph.add_edges([(0, 4), (0,1), (1, 5), (2, 3), (2, 5), (2, 6), (3, 6), (3, 7), (5, 6), (6, 7)])

    generator_tree = bfs_generator_tree(graph, 2)
    generator_tree.vs['label'] = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    
    igraph.plot(generator_tree, layout=generator_tree.layout('tree'), bbox=(800, 800), margin=50, vertex_label_dist=0, vertex_size=40, target="generator_tree.png")


def all_distances():
    graph = igraph.Graph(8)
    graph.add_edges([(0, 4), (0,1), (1, 5), (2, 3), (2, 5), (2, 6), (3, 6), (3, 7), (5, 6), (6, 7)])

    distances = []

    for i in range(8):
        _, _, cur_distances = breadth_first_search(graph, i)
        distances.append(cur_distances)
    
    for d in distances:
        print(d)

    print(f'Diâmetro: {graph_diameter(distances)}')
    print(f'Distância Média: {graph_average_path_length(distances, len(distances[0]))}')

def assignment_06():
    generating_tree()
    all_distances()

if __name__ == '__main__':
    assignment_06()