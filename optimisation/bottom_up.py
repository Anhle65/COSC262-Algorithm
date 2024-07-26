"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
import imp
from re import T
import numpy as np

from sympy import besseli


INFINITY = float('inf')  

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    table = [n_cols * [0] for row in range(n_rows)]
    # for i in range(n_rows):
    #     for j in range(n_cols):
    #         if i == 0:
    #             table[i][j] = 0
    #         elif j < i:
    #             table[i][j] = 1 + table[i - 1][j]
    #         else:
    #             table[i][j] = 2 + table[i - 1][j - i]
    # # **** Your code goes here. It must compute a value 'best', which is
    # # the minimum cost from the top of the grid to the bottom.
    # best = grid[n_rows - 1,0]
    # for k in range(n_rows):
    #     if grid[n_cols - 1, k] < best:
    #         best = grid[n_cols - 1][k]
    # return best
    for j in range(n_cols):
        table[0][j] = grid[0][j]
    table = np.zeros((n_rows, n_cols), dtype=int)  # A numpy table/matrix.
    
    # Now fill it using the recurrence equation.
    # Row 0 is already zero, so don't really need to do it, but to make the
    # code as general as possible, we'll plug the zeros in (again).
    for i in range(n_rows):  # For each row
        for j in range(n_cols):   # For each column
            # Evaluate the recurrence equation to fill in the table value.
            if i == 0:            
                table[i, j] = 0   # Base case (redundant, since already 0)
            elif j < i:
                table[i, j] = 1 + table[i - 1, j]
            else:
                table[i, j] = 2 + table[i - 1, j - i]
    return min(table[-1]) 

    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

print(file_cost('grid'))