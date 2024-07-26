

class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
def max_value(items, capacity, n=None):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
       
    # *** IMPLEMENT ME ***
    result = []
    if n == None:
        n = len(items) + 1
    table = [[0] * (capacity +1)for row in range(n)]
    for row in range(n):
        for col in range(capacity + 1):
            if row == 0 or col == 0:
                table[row][col] = 0
            else:
                weight = items[row - 1].weight
                value = items[row - 1].value
                if weight > col:
                    table[row][col] = table[row -1][col]
                else:
                    table[row][col] = max(value + table[row - 1][col - weight], table[row - 1][col])
    current_value = capacity
    for i in range(len(table) - 1, 0,-1):
        if table[i][current_value] > table[i-1][current_value]:
            result.append(items[i-1])
            current_value -= items[i-1].weight
    return table[-1][-1], result


items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
maximum, selected_items = max_value(items, 10)
print(selected_items)
print(maximum)