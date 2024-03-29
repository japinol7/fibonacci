"""Calculates the n element of the Fibonacci sequence.
The Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Where F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.
So, each term greater than 1 is generated by adding the previous two terms.
For example, the 6th element of the sequence is 8.
It uses a dynamic programming memoized solution for a recursive approach using a list.
Benchmarks function fib with the user created function time_it.
"""
__author__ = 'Joan A. Pinol  (japinol)'

from fibonacci.time_it import time_it


def fib_n(n, memo):
    if memo[n]:
        return memo[n]
    if n < 2:
        return n
    else:
        res = fib_n(n - 1, memo) + fib_n(n - 2, memo)
    memo[n] = res
    return res


def fib(n):
    if n < 0:
        return None
    memo = [None] * (n + 1)
    return fib_n(n, memo)


if __name__ == "__main__":
    n = 35
    res = time_it(fib, n)
    print(f'fib({n}): {res}')
