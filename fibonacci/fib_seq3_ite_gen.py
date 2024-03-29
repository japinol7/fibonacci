"""Calculates the first n elements of the Fibonacci sequence.
The Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Where F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.
So, each term greater than 1 is generated by adding the previous two terms.
For example, the 6th element of the sequence is 8.
It uses an iterative programming solution using a user generator
to yield all Fibonacci numbers from 1 to n.
Benchmarks function fib with the user created decorator time_it.
"""
__author__ = 'Joan A. Pinol  (japinol)'

from fibonacci.time_it_dec import time_it


def fib(n):
    yield 0
    if n > 0:
        yield 1
    last_n = 0
    next_n = 1
    for _ in range(1, n):
        last_n, next_n = next_n, last_n + next_n
        yield next_n


@time_it
def fib_list(n):
    if n < 0:
        return []
    return list(fib(n))


if __name__ == "__main__":
    n = 35
    res = fib_list(n)
    print(f'fib({n}): {res}')
