import igraph
from lib.graph_hamiltonian_cicles import dirac, ore, bondy_and_chvatal


def test_hamiltonian_cycle(graph, graph_label=None):
    if graph_label:
        print(graph_label.center(32, ' '))
    print('Dirac: '.rjust(17, ' ') + str(dirac(graph)))
    print('Ore: '.rjust(17, ' ') + str(ore(graph)))
    print('Bondy & Chvátal: ' + str(bondy_and_chvatal(graph)))

def assignment_03():
    graph1 = igraph.Graph(7, [(0, 1), (0, 2), (0, 5), (0, 6), (1, 2), (1, 3), (1, 5), (2, 3), (2, 4), (3, 4), (3, 6), (4, 5), (4, 6), (5, 6)])
    test_hamiltonian_cycle(graph1, 'Graph 1')
    print()

    graph2 = igraph.Graph(7, [(0, 1), (0, 2), (0, 5), (0, 6), (1, 2), (1, 3), (1, 5), (2, 3), (3, 4), (3, 6), (4, 5), (4, 6), (5, 6)])
    test_hamiltonian_cycle(graph2, 'Graph 2')
    print()

    graph3 = igraph.Graph(7, [(0, 1), (0, 2), (0, 5), (0, 6), (1, 2), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)])
    test_hamiltonian_cycle(graph3, 'Graph 3')
    print()
    
    graph4 = igraph.Graph(7, [(0, 1), (0, 2), (0, 5), (0, 6), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
    test_hamiltonian_cycle(graph4, 'Graph 4')
    print()


if __name__ == '__main__':
    assignment_03()
