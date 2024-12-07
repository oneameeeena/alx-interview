#!/usr/bin/python3
"""Island Perimeter Problem."""


def island_perimeter(grid):
    """
     Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A list of list of integers where:
            - 0 represents water
            - 1 represents land
            - Each cell is a square with side length of 1
            - Cells are connected horizontally/vertically (not diagonally)
            - Grid is rectangular with width and height not exceeding 100
            - Grid is completely surrounded by water
            - There is only one island or no island
            - The island doesn’t have lakes (water inside that isn’t connected
              to the water surrounding the island)

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:  # Checking the top
                    perimeter += 1
                if (
                    row == rows - 1 or grid[row + 1][col] == 0
                ):  # Checking the bottom
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:  # Checking the left
                    perimeter += 1
                if (
                    col == cols - 1 or grid[row][col + 1] == 0
                ):  # Checking the right
                    perimeter += 1
    return perimeter
