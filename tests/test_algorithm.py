"""
This file contains the different tests
over the algorithms created in src/algorithm.py
"""

# Imports
import python_package.algorithm as alg

# Tests
def test_sum_list():
    assert alg.naive_count([1, 2, 3, 4, 5]) == 15

def test_n_largest():
    assert alg.n_largest([1, 2, 3, 4, 5], 3) == [3, 4, 5]

def test_n_largest_all():
    assert alg.n_largest([1, 2, 3, 4, 5], 10) == [1, 2, 3, 4, 5]