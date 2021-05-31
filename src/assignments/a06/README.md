[PT-BR](README.pt-br.md)
# Graph diameter
This repo refers to an assignment for a Graph Theory course at University of Fortaleza.  

# Assignment description
Given the [graph](graph.png):  
* Calculate the graph diameter using the breadth first search algorithm  
* Calculate the graph average path length using the breadth first search algorithm  
* Plot the breadth first search generator tree (tree representing the order in which the vertices are searched) of the graph  

# Solution
For ease of calculation, vertices [r, s, t, u, v, w, x, y] were called respectively [0, 1, 2, 3, 4, 5, 6, 7]  
The `all_distances` function simply calls the `breadth_first_search` for each vertex in the graph and builds a 2 dimension array all_distances where all_distances[i][j] is the distance between vertices i and j, then calculates the diameter based on the max distance.  
The [`bfs_generator_tree`](src/util/BFS.py) function is a modified `breadth_first_search` that returns the generator_tree as an igraph.Graph.  
The diameter and average path length functions were implemented at [graph_utils.py](src/util/graph_utils.py).  

# Running the code
Inside the root folder:
```sh
# Create a python virtual environment
$ python -m venv .venv
# Activate the virtual environment
$ ./.venv/Scripts/activate
# Install dependencies
$ pip install -r requirements.txt
# Run the main script
$ python ./src/main.py
```

