[PT-BR](README.pt-br.md)
# Breadth First Search Assignment
This repo refers to an assignment for a Graph Theory course at University of Fortaleza.  

# Assignment description
Given the [graph](graph.png):  
* Using vertex `s` as origin, show the resulting values of d (distances array) and ¶ (parents array) resulting from the BFS algorithm
* Applying the BFS algorithm using the vertices `x` and `t` as origin, print the vertices queue at each iteration

# Solution
For ease of calculation, vertices [r, s, t, u, v, w, x, y] were called respectively [0, 1, 2, 3, 4, 5, 6, 7]  
The `breadth_first_search` function was implemented at [src/util/BFS.py](src/util/BFS.py) and takes as parameters the graph of type igraph.Graph (graph that will be searched), origin of type int (origin index of where to start the bfs) and print_queue of type boolean (this is used for the 2nd part of the assignment where printing the queue is necessary).  
The `main` function at [main.py](src/main.py) simply calls the `breadth_first_search` algorithm passing the graph shown in the image three times using 1 (s), 2 (t) and 6 (x) as origin values as per the assignment description printing the d and ¶ arrays for origin 1 and printing the queue for origins 2 and 6.  

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

