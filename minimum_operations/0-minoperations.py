#!/usr/bin/python3
"""
  In a text file, there is a single character H. Your text editor can execute only two operations in this file:
  Copy All and Paste. Given a number n,
  write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
  """


def minOperations(n):
    # for n=0 or n=1
    if n <= 1:
        return 0

    # loop to find prime factors (smaller number)
    for i in range(2, int((n / 2) + 1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i
    return n
