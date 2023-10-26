"""
This file contains different algorithms in order to 
be prepared for future opportunities.
"""

# Imports
import numpy as np
import pandas as pd
from python_package.utils import timer, mean_timer



# Functions
@timer
def naive_count(list_to_sum: list):
    """
    This function sums all the elements in a list.
    """
    total = 0
    for i in list_to_sum:
        total += i
    return total

#@timer
@mean_timer()
def n_largest(ordered_list, n):
    return ordered_list[-n:]

#@timer
@mean_timer()
def n_largest_len_test(ordered_list, n):
    if n >= len(ordered_list):
        return ordered_list
    return ordered_list[-n:]



# Main
if __name__ == "__main__":
    list_len = 30
    n_largest_len = 3
    my_list = list(range(list_len))
    n_largest(my_list, n_largest_len)
    n_largest_len_test(my_list, n_largest_len)