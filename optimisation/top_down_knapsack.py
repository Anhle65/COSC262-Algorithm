import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
        
def max_value(items, capacity, index = None, cache = None):
    if cache == None:
        cache = {}
    if index == None:
        index = len(items)
    if index == 0 or capacity == 0:
        return 0
    elif items[index - 1].weight > capacity:
        return max_value(items, capacity, index - 1, cache)
    else:
        if (index, capacity) in cache:
            return cache[(index, capacity)]
        value = max(max_value(items, capacity, index -1, cache), items[index-1].value + \
                    max_value(items, capacity - items[index - 1].weight, index - 1, cache))
        cache[(index, capacity)] = value
    return cache[(index, capacity)]

 	

# A large problem (500 items)
import random
random.seed(12345)  # So everyone gets the same

items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
print(max_value(items, 500))


items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

print(max_value(items, 10))