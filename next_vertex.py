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
in_tree = [False, True, True, True, True]
distance = [math.inf, 0, 3, 12, 5]
print(next_vertex(in_tree, distance))