import numpy as np


def adj_matrix_to_inc_matrix(adj_matrix):
    """Матрица смежности → Матрица инцидентности"""
    n = len(adj_matrix)
    # Собираем все дуги
    edges = []
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                edges.append((i, j))

    m = len(edges)
    inc_matrix = [[0] * m for _ in range(n)]

    for k, (i, j) in enumerate(edges):
        inc_matrix[i][k] = 1  # дуга выходит
        inc_matrix[j][k] = -1  # дуга входит

    return inc_matrix


def adj_matrix_to_adj_list(adj_matrix):
    """Матрица смежности → Список смежности"""
    n = len(adj_matrix)
    adj_list = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list


def adj_matrix_to_edge_list(adj_matrix):
    """Матрица смежности → Список дуг"""
    n = len(adj_matrix)
    edges_from = []
    edges_to = []
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                edges_from.append(i)
                edges_to.append(j)
    return np.array(edges_from), np.array(edges_to)


def inc_matrix_to_adj_matrix(inc_matrix):
    """Матрица инцидентности → Матрица смежности"""
    n = len(inc_matrix)  # количество вершин
    m = len(inc_matrix[0])  # количество дуг
    adj_matrix = [[0] * n for _ in range(n)]

    for edge_idx in range(m):
        start = None
        end = None
        for vertex in range(n):
            if inc_matrix[vertex][edge_idx] == 1:
                start = vertex
            elif inc_matrix[vertex][edge_idx] == -1:
                end = vertex
        if start is not None and end is not None:
            adj_matrix[start][end] = 1
    return adj_matrix


def inc_matrix_to_adj_list(inc_matrix):
    """Матрица инцидентности → Список смежности"""
    adj_matrix = inc_matrix_to_adj_matrix(inc_matrix)
    return adj_matrix_to_adj_list(adj_matrix)


def inc_matrix_to_edge_list(inc_matrix):
    """Матрица инцидентности → Список дуг"""
    n = len(inc_matrix)
    m = len(inc_matrix[0])
    edges_from = []
    edges_to = []

    for edge_idx in range(m):
        start = None
        end = None
        for vertex in range(n):
            if inc_matrix[vertex][edge_idx] == 1:
                start = vertex
            elif inc_matrix[vertex][edge_idx] == -1:
                end = vertex
        if start is not None and end is not None:
            edges_from.append(start)
            edges_to.append(end)

    return np.array(edges_from), np.array(edges_to)



def adj_list_to_adj_matrix(adj_list):
    """Список смежности → Матрица смежности"""
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]
    for i in adj_list:
        for j in adj_list[i]:
            adj_matrix[i][j] = 1
    return adj_matrix


def adj_list_to_inc_matrix(adj_list):
    """Список смежности → Матрица инцидентности"""
    adj_matrix = adj_list_to_adj_matrix(adj_list)
    return adj_matrix_to_inc_matrix(adj_matrix)


def adj_list_to_edge_list(adj_list):
    """Список смежности → Список дуг"""
    edges_from = []
    edges_to = []
    for i in adj_list:
        for j in adj_list[i]:
            edges_from.append(i)
            edges_to.append(j)
    return np.array(edges_from), np.array(edges_to)



def edge_list_to_adj_matrix(edges_from, edges_to, n=5):
    """Список дуг → Матрица смежности"""
    adj_matrix = [[0] * n for _ in range(n)]
    for i in range(len(edges_from)):
        adj_matrix[edges_from[i]][edges_to[i]] = 1
    return adj_matrix


def edge_list_to_inc_matrix(edges_from, edges_to, n=5):
    """Список дуг → Матрица инцидентности"""
    m = len(edges_from)
    inc_matrix = [[0] * m for _ in range(n)]
    for k in range(m):
        inc_matrix[edges_from[k]][k] = 1
        inc_matrix[edges_to[k]][k] = -1
    return inc_matrix


def edge_list_to_adj_list(edges_from, edges_to, n=5):
    """Список дуг → Список смежности"""
    adj_list = {i: [] for i in range(n)}
    for i in range(len(edges_from)):
        adj_list[edges_from[i]].append(edges_to[i])
    return adj_list




def convert_graph(graph, source_type, target_type):

    if source_type == 'adj_matrix':
        if target_type == 'adj_matrix':
            return graph
        elif target_type == 'inc_matrix':
            return adj_matrix_to_inc_matrix(graph)
        elif target_type == 'adj_list':
            return adj_matrix_to_adj_list(graph)
        elif target_type == 'edge_list':
            return adj_matrix_to_edge_list(graph)


    elif source_type == 'inc_matrix':
        if target_type == 'adj_matrix':
            return inc_matrix_to_adj_matrix(graph)
        elif target_type == 'inc_matrix':
            return graph
        elif target_type == 'adj_list':
            return inc_matrix_to_adj_list(graph)
        elif target_type == 'edge_list':
            return inc_matrix_to_edge_list(graph)


    elif source_type == 'adj_list':
        if target_type == 'adj_matrix':
            return adj_list_to_adj_matrix(graph)
        elif target_type == 'inc_matrix':
            return adj_list_to_inc_matrix(graph)
        elif target_type == 'adj_list':
            return graph
        elif target_type == 'edge_list':
            return adj_list_to_edge_list(graph)


    elif source_type == 'edge_list':
        edges_from, edges_to = graph
        if target_type == 'adj_matrix':
            return edge_list_to_adj_matrix(edges_from, edges_to)
        elif target_type == 'inc_matrix':
            return edge_list_to_inc_matrix(edges_from, edges_to)
        elif target_type == 'adj_list':
            return edge_list_to_adj_list(edges_from, edges_to)
        elif target_type == 'edge_list':
            return graph

    else:
        raise ValueError(f"Неизвестный тип представления: {source_type} или {target_type}")
