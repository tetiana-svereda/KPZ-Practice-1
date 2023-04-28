import pytest
from lab2 import prime_num_generator

def test_first_twelve_primes():
    gen = prime_num_generator()
    first_twelve_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in range(12):
        assert next(gen) == first_twelve_primes[i]

    gen1 = prime_num_generator()
    for i in range(100):
        next(gen1)
    assert next(gen1) == 547