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


# def permutations(s):
#     solutions = []
#     dfs_backtrack((), s, solutions)
#     return solutions


def dfs_backtrack(candidate_path, input_data, output_data, destination):
    if should_prune(candidate_path):
        return
    if is_solution(candidate_path, destination):
        add_to_output(candidate_path, output_data)
    else:
        for child_candidate in children(candidate_path, input_data):
            dfs_backtrack(child_candidate, input_data, output_data, destination)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate_path, destination):
    """Returns True if the candidate is a complete solution"""
    return destination == candidate_path[-1]


def children(candidate_path, adj_list):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    result = []
    last_vertex = candidate_path[-1]
    for element in adj_list:
        
        if last_vertex not in adj_list:
            result.append(adj_list[last_vertex])
    return result

def all_paths(adj_list, source, destination):
    solution = []
    dfs_backtrack((source,), adj_list, solution, destination)
    return solution

triangle_graph_str = """\
U 3
0 1
1 2
2 0
"""

adj_list = adjacency_list(triangle_graph_str)
print(sorted(all_paths(adj_list, 0, 2)))
print(all_paths(adj_list, 1, 1))