import numpy as np

print("1а. Матрица смежности")
adj_matrix = np.array([
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
], dtype=int)
print(adj_matrix)
print()

print("1б. Матрица инцидентности")
inc_matrix = np.array([
    [-1,  0,  0,  0, -1,  1,  1,  0,  0],  # вершина 0
    [ 1, -1,  0,  0,  0,  0,  0, -1,  0],  # вершина 1
    [ 0,  0,  0,  1,  1,  0,  0,  1,  1],  # вершина 2
    [ 0,  1,  1,  0,  0, -1,  0,  0, -1],  # вершина 3
    [ 0,  0, -1, -1,  0,  0, -1,  0,  0]   # вершина 4
], dtype=int)
print(inc_matrix)
print()

print("1в. Список смежности")
adj_list = {
    0: [3, 4],
    1: [0],
    2: [0, 4, 1, 3],
    3: [1, 4],
    4: []
}
for key in sorted(adj_list.keys()):
    print(f"{key}: {adj_list[key]}")
print()

print("1г. Список дуг")
edges_from = np.array([1, 3, 3, 2, 2, 0, 0, 2, 2])
edges_to   = np.array([0, 1, 4, 4, 0, 3, 4, 1, 3])
print("from:", edges_from)
print("to:  ", edges_to)
print()

print("1д. Упорядоченный список дуг")
edges = [(1,0), (3,1), (3,4), (2,4), (2,0), (0,3), (0,4), (2,1), (2,3)]

edges_sorted = sorted(edges)

ordered_num = np.array([0,1, 2, 3, 4, 5, 6, 7, 8])
ordered_from = np.array([e[0] for e in edges_sorted])
ordered_to   = np.array([e[1] for e in edges_sorted])

print("№:    ", ordered_num)
print("from: ", ordered_from)
print("to:   ", ordered_to)
print()

numbr = np.array([0, 1, 2, 3, 4, 5])
s = np.array([0, 2, 3, 7, 9, 9])

print("№:  ", numbr)
print("s:  ", s)
