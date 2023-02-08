**Min Operations**
A method to calculate the fewest number of operations needed to result in exactly n H characters in a text file.

Usage
`minOperations(n)`

Input
`n`: an integer, the target number of `H` characters in the text file

Output
An integer representing the minimum number of operations needed. If `n` is impossible to achieve, the function returns `0`.

Example

>>> minOperations(7)
7

>>> minOperations(10)
5

>>> minOperations(-5)
0 

**Explanation**
This method uses the idea that the minimum number of operations is equal to the sum of all the prime factors of n. The code finds the smallest prime factor of n and divides n by that factor, adding the factor to the number of operations. This process is repeated until n is no longer divisible. The remaining value of n is also added to the number of operations.



