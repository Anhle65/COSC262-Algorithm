# def combinations(items, r = 2, index = 0, result = None):
#     if result == None:
#         result = []
#     if r == 0:
#         return [result]
#     for i in range(index, len(items)):
#         result+[items[i]]
#         combinations(items, r-1, index+1, result)
#     # for i in a:
#     #     result.append()
#     # print(result)
#     return result

# print(combinations([1,2,3], 1))

# def all_subsets(s, lenght = 1, final = None):
#     if final == None:
#         final = [[]]
#     if lenght > len(s):
#         return [set(ele) for ele in final]
#     else:
#         subsets = combinations(list(s), lenght)
#         for each in subsets:
#             final.append(each)
#         all_subsets(list(s), lenght + 1, final)
#     return [set(ele) for ele in final]

# def combinations(items, r, start=0, combo=None):
#     if combo is None:
#         combo = []
#     if r == 0:
#         return [combo]
#     result = []
#     for i in range(start, len(items)):
        
#         # print(combo + [items[i]])
#         result.extend(combinations(items, r - 1, i + 1, combo + [items[i]]))
#     # print(result)
#     return result

# def all_subsets(s):
#     in_list = list(s)
#     final = [[]]
#     for length in range(1, len(in_list) + 1):
#         subsets = combinations(in_list, length)
#         final.extend(subsets)
#         # print(final)
#     return [set(subset) for subset in final]
# print(sorted(map(sorted, all_subsets({1,2,3,4}))))
# print(all_subsets({}))
# print(all_subsets({'a', 'b'}))
# print({1} in all_subsets({0, 1, 2}))

def small_sub(items, size, start = 0, result = []):
    temp = []
    if size == 0:
        return [result]
    for i in range(start, len(items)):       
        result += [items[i]]
        small_sub(items, size - 1, start + 1,result)
    print(result)
    return result
def subsets(items):
    final = []
    result = small_sub(items, size=1)
    # for i in range(len(items)):
    #     for each in result:
    #         final += [each +[items[i]]]
            # print(final)
# print(small_sub([1,2,3]))
subsets([1,3,2])
