#!/usr/bin/python3
def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle list with the first row
    triangle = [[1]]

    # Generate each subsequent row using the previous row
    for i in range(1, n):
        # Create a new row with i+1 elements, initially filled with 0
        row = [0] * (i+1)
        # Set the first and last elements of the row to 1
        row[0] = row[-1] = 1
        # Calculate the middle elements of the row based on the previous row
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        # Append the completed row to the triangle list
        triangle.append(row)

    return triangle