#!/usr/bin/python3

"""
    Generates a Pascal's Triangle with n rows.
    Args:
        n (int): The number of rows in the triangle.
    Returns:
        A list of lists representing the Pascal's Triangle with n rows.
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [0] * (i + 1)
        row[0] = row[-1] = 1
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle