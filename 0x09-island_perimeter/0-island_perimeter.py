#!/usr/bin/python3
"""
Island Perimeter Module
"""


def island_perimeter(grid):
    """returns the perimeter of an island described in grid"""
    perimeter = 0
    grid_len = len(grid)
    for row in range(grid_len):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row - 1 < 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if col - 1 < 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col + 1 >= len(grid[row]) or grid[row][col + 1] == 0:
                    perimeter += 1
                if row + 1 >= grid_len or grid[row + 1][col] == 0:
                    perimeter += 1
    return perimeter
