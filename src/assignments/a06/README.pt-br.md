[EN-US](README.md)
# Trabalho sobre diâmetro de grafos
Este repositório refere-se a um trabalho para a cadeira de Teoria dos Grafos na Universidade de Fortaleza.

# Descrição do Trabalho
Dado o [grafo](graph.png):  
* Calcular o diâmetro do grafo utilizando o algorítmo breadth first search  
* Calcular a distância média do grafo utilizando o algorítmo breadth first search  
* Plotar a árvore geradora (árvore represendanto a ordem em que os vértices são buscados) da breadth first search  

# Resolução
Por comodidade, os vértices [r, s, t, u, v, w, x, y] são chamados respectivamente [0, 1, 2, 3, 4, 5, 6, 7]  
A função `all_distances` simplesmente chama a função `breadth_first_search` para cada vértice no grafo e constrói uma lista de 2 dimensões all_distances onde all_distances[i][j] é a distância entre os vértices i e j, então calcula o diâmetro baseado na distância máxima.  
A função [`bfs_generator_tree`](src/util/BFS.py) é uma modificação da função `breadth_first_search` que retorna a árvore geradora como um igraph.Graph.  
As funções diameter (diâmetro) e average path length (distância média) foram implementadas em [graph_utils.py](src/util/graph_utils.py).

# Executando o código
Dentro da pasta raiz:
```sh
# Criar um ambiente virtual (virtual environment) do python
$ python -m venv .venv
# Ativar o ambiente virtual
$ ./.venv/Scripts/activate
# Instalar as dependências
$ pip install -r requirements.txt
# Executar o script main
$ python ./src/main.py
```

