## Fibonacci

    Benchmarks some algorithms that calculate elements of the Fibonacci sequence.
	The Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
	Where:
		F(0) = 0,  F(1) = 1
		F(n) = F(n - 1) + F(n - 2) for n > 1

    So, each term greater than one is generated by adding the previous two terms.
    For example, the 6th element of the sequence is 8.

    Most algorithms contained here do not expect negative numbers;
    so, if a negative number is supplied their behavior is undefined.

	version: 1.0.1
	author: Joan A. Pinol
	author_nickname:  japinol
	author_gitHub: japinol7
	author_twitter: @japinol
	Python requires: 3.6 or greater.
	Python versions tested: 3.7.3 64bits under Windows 10

## Scripts:

    The algorithms are in the folder fibonacci (as a package) in each own module
    and are imported to benchmark them:

    > fib_n_term.py:
        Benchmarks some algorithms that calculate the n element of the Fibonacci sequence.
        	1.  fib1_rec.py
               A recursive approach without optimizations.
        	2.  fib2_ite.py
               An iterative programming solution.
        	3a. fib3a_rec_mem_list.py
               A dynamic programming memoized solution
               for a recursive approach using a list.
        	3b. fib3b_rec_mem_arr.py
               A dynamic programming memoized solution for a recursive approach
               using an array of unsigned integers of 64 or 32 bits.
        	4.  fib4_rec_mem_dic.py
               A dynamic programming memoized solution using a dictionary.
        	5.  fib5_rec_mem.py
               A dynamic programming memoized solution for a recursive approach
               using functools.lru_cache from the standard library.
        	6.  fib6_rec_mem.py
               A dynamic programming memoized solution for a recursive approach
               using functools.lru_cache from the standard library.
               Benchmarks function fib with the user created decorator time_it.

    > fib_sequence.py:
        Benchmarks some algorithms that calculate the first n elements of the Fibonacci sequence.
        	1. fib_seq1_ite.py
                It uses an iterative programming solution and returns the sequence as a list.
        	2. fib_seq2_ite.py
                An iterative programming solution using a list in the very algorithm.
        	3. fib_seq3_ite_gen.py
                An iterative programming solution using a user generator.

    > fib_n_sum.py:
        Benchmarks some algorithms that calculate the sum of then even-valued terms of the Fibonacci sequence
        	1. fib_sum1_ite.py
                An iterative programming solution.
        	2. fib_sum2_ite.py
                An iterative programming solution using a list in the very algorithm.
