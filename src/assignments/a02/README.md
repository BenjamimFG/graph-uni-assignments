# Grafo Estados Brasileiros
Projeto referente ao trabalho 2 da disciplina de Resolução de Problemas com Grafos.

# Especificação do trabalho
> Escolher 2 formas de representação computacional descritas no arquivo “Aula 3” e implementar um grafo para representar os Estados do Brasil que são vizinhos.
>
> Após representar computacionalmente:  
>   -plotar o grafo e  
>   -plotar em forma de Histograma a frequência dos graus


# Representações
Representação dos estados brasileiros limítrofes é feita através de uma Matriz de Adjacência e de uma Matriz de Incidência.

# Plotagem
Ambos os grafos gerados a partir das matrizes de adjacência e incidência são plotados para os arquivos png "Grafo Matriz de Adjacência.png" e "Grafo Matriz de Incidência.png" respectivamente.

É plotado também em tela o histograma com as frequências dos graus de cada vértice do grafo.

# Rodando o código
criar virtual environment do python:
```shell
$ python -m venv .venv
```

ativar virtual environment:
```shell
$ .venv/Scripts/activate
```

instalar dependências:
```shell
$ pip install -r requirements.txt
```

executar arquivo main:
```shell
$ python src/main.py
```