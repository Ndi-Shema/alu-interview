#!/usr/bin/python3
def minOperations(n):
    """
    Returns
        int
    """
    if type(n) is not int or n <= 0:
        return 0
    operations = 0
    H = 1
    copy_all = 0
    paste = 0
    H_copied = 0
    while H < n:
        if n % H == 0:
            copy_all += 1
            H_copied = H
        paste += 1
        operations = copy_all + paste
        H += H_copied
    return operations

print(minOperations.__doc__)
