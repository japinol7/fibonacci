'''Calculates the sum of the n even-valued terms of the Fibonacci sequence
by considering only the terms whose values do not exceed twelve million.
The Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Where F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.
So, each term greater than 1 is generated by adding the previous two terms.
For example, the 6th element of the sequence is 8.
It uses an iterative programming solution using a list in the very algorithm.
Benchmarks function fib_sum with the user created decorator time_it.
'''
__author__ = 'Joan A. Pinol  (japinol)'

from fibonacci.time_it_dec import time_it


@time_it
def fib_sum(limit):
    fib_numbers = [0, 1, 1, 2]
    while fib_numbers[-1] < limit:
        fib_numbers += [fib_numbers[-1] + fib_numbers[-2]]
    del fib_numbers[-1]

    total_sum = 0
    for fib_number in fib_numbers:
        if fib_number % 2 == 0:
            total_sum += fib_number
    return total_sum


if __name__ == "__main__":
    limit = 12_000_000   # Top limit for the terms' values
    res = fib_sum(limit)
    print(f'fib({limit:}): {res:}')
