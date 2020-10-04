'''***GFG***
~ => Prime functions in Python SymPy

isprime(n) : It tests if n is a prime number (True) or not (False).
primerange(a, b) : It generates a list of all prime numbers in the range [a, b).
randprime(a, b) : It returns a random prime number in the range [a, b).
primepi(n) : It returns the number of prime numbers less than or equal to n.
prime(nth) : It returns the nth prime, with the primes indexed as prime(1) = 2. The nth prime is approximately n*log(n) and can never be larger than 2**n.
prevprime(n) : It returns the prev prime smaller than n.
nextprime(n) : It returns the next greater prime than n.
sieve.primerange(a, b) : It generates all prime numbers in the range [a, b), implemented as a dynamically growing sieve of Eratosthenes.
filter_none

'''

import sympy

print(sympy.prime(10001))
