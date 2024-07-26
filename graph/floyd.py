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
import math
import copy
def floyd(distance):
    new_distance = copy.deepcopy(distance)
    length = len(distance)
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if new_distance[i][j] > new_distance[i][k] + new_distance[k][j]:
                    new_distance[i][j] = new_distance[i][k] + new_distance[k][j]
    return new_distance
import pprint

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))