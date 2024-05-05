import math


def adjacency_list(graph_str):
    graph = graph_str.strip().split("\n")
    header = graph[0].split(" ")
    parent = [None]*int(header[1])
    isUndirected = True
    if header[0] == "D":
        isUndirected = False
    for each in graph[1:]:
        edge = each.split(" ")
        if len(edge) == 2:
            weighted = None
        else:
            weighted = int(edge[2])
        if parent[int(edge[0])] is None:
            parent[int(edge[0])] = [(int(edge[1]), weighted)]
        else:
            parent[int(edge[0])].append((int(edge[1]), weighted))
        if isUndirected:
            if parent[int(edge[1])] is None:
                parent[int(edge[1])] = [(int(edge[0]), weighted)]
            else:
                parent[int(edge[1])].append((int(edge[0]), weighted))
    for i in range(len(parent)):
        if parent[i] == None:
            parent[i] = []
    return parent

def distance_matrix(adj_list):
    result = [[math.inf]*len(adj_list) for _ in range(len(adj_list))]
    for i in range(len(adj_list)):
        result[i][i] = 0
        for v in adj_list[i]:
            result[i][v[0]] = v[1]
    return result
graph_str = """\
U 3 W
0 1 5
2 1 7
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))

# more readable output (less readable code):
print("\nEach row on a new line:")
print("\n".join(str(lst) for lst in distance_matrix(adj_list)))