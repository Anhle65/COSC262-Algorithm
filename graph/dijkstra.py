import math
def next_vertex(in_tree, distance):
    smallest = math.inf
    vertex = None
    for index in range(len(in_tree)):
        if in_tree[index] == False:
            if smallest >= distance[index]:
                smallest = distance[index]
                vertex = index
    return vertex
def dijkstra(adj_list, start):
    vertices = len(adj_list)
    in_tree = [False]*vertices
    distance = [math.inf]*vertices
    parent = [None]*vertices
    distance[start] = 0
    while False in in_tree:
        vertex = next_vertex(in_tree, distance)
        in_tree[vertex] = True
        for v, w in adj_list[vertex]:
            if not in_tree[v] and (distance[vertex] + w) < distance[v]:
                distance[v] = distance[vertex] + w
                parent[v] = vertex
    return (parent, distance)