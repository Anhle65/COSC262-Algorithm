def sequence_length(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return sequence_length(n/2) + 1
    return sequence_length(3*n+1) + 1 
# print(sequence_length(1))
def recursive_divide(x, y):
    if x < y:
        return 0
    return recursive_divide(x-y, y) + 1
# print(recursive_divide(160, 3))
def my_enumerate(items, start=0, end = None):
    end = len(items)
    if end == start:
        return []
    return [(start, items[start])] + my_enumerate(items, start+1, end)
# ans = my_enumerate([10, 20, 30])
# print(ans)    
# ans = my_enumerate(['dog', 'pig', 'cow'])
# print(ans)
# ans = my_enumerate([])
# print(ans)
def inner_loop(list1, list2):
    if len(list2) == 0:
        return []
    return [(list1[0], list2[0])] + inner_loop(list1, list2[1:])

def all_pairs(list1, list2):
    if len(list1) == 0:
        return []
    return inner_loop(list1, list2) + all_pairs(list1[1:], list2)
# print(all_pairs([1, 2], [10, 20, 30]))
def perms(items, length =0, result = None):
    if result is None:
        result = []
    if length == len(items):
        return [()]
    for i in range(length, len(items)):
        items[i], items[length] = items[length], items[i]
        element = tuple(items)
        if element not in result:
            result.append(element)
    for each in result:
        perms(list(each), length + 1, result)
    return result
t= perms([1, 2, 3,4])
for perm in sorted(t):
    print(perm)
print(len(t))