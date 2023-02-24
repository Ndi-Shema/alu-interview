#!/usr/bin/python3

"""Rain calculation."""

def rain(walls):
    n = len(walls)
    if n == 0:
        return 0

    stack = []
    total_water = 0

    for i in range(n):
        while stack and walls[i] > walls[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(walls[i], walls[stack[-1]]) - walls[top]
            total_water += distance * bounded_height

        stack.append(i)

    return total_water
