[EN-US](README.md)
# Trabalho sobre Breadth First Search
Este repositório refere-se a um trabalho para a cadeira de Teoria dos Grafos na Universidade de Fortaleza.

# Descrição do Trabalho
Dado o [grafo](graph.png):  
* Utilizando o vértice `s` como origem, mostre os valores de d (array de distâncias) e ¶ (array de parentes) resultantes do algorítmo BFS
* Aplicando o algorítmo BFS utilizando os vértices `x` e `t` como origem, imprima a cada iteração a fila de vértices

# Resolução
Por comodidade, os vértices [r, s, t, u, v, w, x, y] são chamados respectivamente [0, 1, 2, 3, 4, 5, 6, 7]  
A função `breadth_first_search` foi implementada em [src/util/BFS.py](src/util/BFS.py) e leva como parâmetros o graph do tipo igraph.Graph (grafo que será buscado), origin do tipo int (indice de início do bfs) e print_queue do tipo boolean (este parâmetro é utilizado para a 2ª parte do trabalho onde imprimir a fila é necessário).  
A função `main` em [main.py](src/main.py) simplesmente chama a função `breadth_first_search` passando o grafo mostrado na imagem e executando os requerimentos descritos.  

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

