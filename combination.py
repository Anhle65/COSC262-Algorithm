def perms(items, length =0, result = None):
    if result is None:
        result = []
    if length == len(items):
        return [()]
    for i in range(length, len(items)):
        items[i], items[length] = items[length], items[i]
        # element = tuple(items)
        if items not in result:
            result.append(items)
    for each in result:
        perms(list(each), length + 1, result)
    return result

def combinations(items, r, index = 0, result = None):
    if result == None:
        result = []
    if len(items) < r:
        return []
    if r == 0:
        if len(items) == 0:
            return []
        return [()]
    if len(items) == r:
        return [tuple(items)]
    if r == 1:
        for i in range(len(items)):
            print(items[i])
            result.append(tuple([items[i]]))
        return result
    if index < len(items):
        element = []
        copy_list = items.copy()
        copy_list.pop(index)
        i = 0
        while len(element) < r:
            element += [copy_list[i]]
            i += 1
        result.append(tuple(element))
        combinations(items, r, index + 1, result)
    return result
ans = []
for combo in combinations([1, 2, 3, 4, 5], 3):
    ans.append(tuple(sorted(combo)))
print(sorted(ans))
print(sorted(combinations([1, 2, 3], 1)))


