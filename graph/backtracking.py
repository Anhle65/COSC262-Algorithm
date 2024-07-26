def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate, input_data):
    """Returns True if the candidate is a complete solution"""
    return len(candidate) == len(input_data)


def children(candidate, input_data):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    result = []
    for each in input_data:
        if each not in candidate:
            result.append(candidate + (each,))
    return result
    
# perms = permutations(set())
# print(len(perms) == 0 or list(perms) == [()])
