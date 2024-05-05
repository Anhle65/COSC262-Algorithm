from adjacency_list import adjacency_list
def dfs_tree(adj_list, start):
    parent = [None]*len(adj_list)
    state = ["U"]*len(adj_list)
    state[start] = "D"
    result, is_connected = dfs_loop(adj_list, start, state, parent)
    return result, is_connected

def dfs_loop(adj_list, u, state, parent):
    is_connected= True
    for vertex in adj_list[u]:
        if state[vertex[0]] == "U":
            state[vertex[0]] = "D"
            parent[vertex[0]] = u
            dfs_loop(adj_list, vertex[0], state, parent)
    state[u] = "P"
    for each in state:
        if each != "P":
            is_connected = False
    return parent, is_connected
def transpose(adj_list):
    transpose_list = [[]]*len(adj_list)
    for i in range(len(adj_list)):
        for v,w in adj_list[i]:
            if transpose_list[v] == []:
                transpose_list[v] = [(i,w)]
            else:
                transpose_list[v].append((i,w))
    return transpose_list
def is_strongly_connected(adj_list):
    traversal, is_connected = dfs_tree(adj_list, 0)
    if not is_connected:
        return False
    transpose_graph = transpose(adj_list)
    transpose_traversal, is_transpose_connected = dfs_tree(transpose_graph, 0)
    return is_transpose_connected
graph_string = """\
U 5
2 4
3 1
0 4
2 1
"""

print(is_strongly_connected(adjacency_list(graph_string)))