#!/usr/bin/python3
 """Return an empty list if n is less than or equal to 0
    Initialize the triangle list with the first row
    Generate each subsequent row using the previous row
    Create a new row with i+1 elements, initially filled with 0
    Set the first and last elements of the row to 1
    Calculate the middle elements of the row based on the previous row
    Append the completed row to the triangle list
    Return the completed triangle list"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [0] * (i+1)
        row[0] = row[-1] = 1
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle