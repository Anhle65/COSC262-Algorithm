from adjacency_list import adjacency_list
def transpose(adj_list):
    transpose_list = [[]]*len(adj_list)
    for i in range(len(adj_list)):
        for v,w in adj_list[i]:
            if transpose_list[v] == []:
                transpose_list[v] = [(i,w)]
            else:
                transpose_list[v].append((i,w))
    return transpose_list
graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))
    
