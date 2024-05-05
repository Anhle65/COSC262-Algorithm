
def no_clashes(lists):
    check = set(lists[0])
    for i in range(1, len(lists)):
        result = (check.difference(set(lists[i])))
    return result
lists = [[1, 5, 9, 5, 0, 9],
         [2, 3, 7, 1, 7, 8, 4, 10, 20],
         [4, 6, 80, 40],
         [0],
         [5]]
result = no_clashes(lists)
print(result)
lists = [[1, 5, 9, 5, 0, 9],
         [2, 3, 7],
         [4, 6, 8, 4]]
result = no_clashes(lists)
print(result)
# Your code must be efficient
# otherwise this test will timeout
list1 = list(range(100000))
list2 = list(range(10,200000))
lists = [list1, list2]
result = no_clashes(lists)
for item in result:
    print(item)