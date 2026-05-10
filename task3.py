import numpy as np

def get_outgoing_edges(graph, rep_type, vertex):
    edges = []

    # 1. Матрица смежности 
    if rep_type == 'adj_matrix':
        for j in range(len(graph[vertex])):
            if graph[vertex][j] == 1:
                edges.append((vertex, j))

    # 2. Матрица инцидентности
    elif rep_type == 'inc_matrix':
        for edge_idx in range(graph.shape[1]):
            if graph[vertex][edge_idx] == 1:
                for v in range(graph.shape[0]):
                    if graph[v][edge_idx] == -1:
                        edges.append((vertex, v))
                        break

    # 3. Список смежности 
    elif rep_type == 'adj_list':
        for neighbor in graph[vertex]:
            edges.append((vertex, neighbor))

    # 4. Список дуг 
    elif rep_type == 'edge_list':
        edges_from, edges_to = graph
        for i in range(len(edges_from)):
            if edges_from[i] == vertex:
                edges.append((edges_from[i], edges_to[i]))

    # 5. Упорядоченный список дуг 
    elif rep_type == 'ordered_list':
        row_ptr, col_ind = graph
        start = row_ptr[vertex]
        end = row_ptr[vertex + 1]
        for idx in range(start, end):
            edges.append((vertex, col_ind[idx]))

    return edges
