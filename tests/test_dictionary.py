"""
faire test difference de temps entre classe Dictionary et builtin {}
Besoin d'ajouter le decorateur sur les fonctions à mesurer
"""

# Imports
from python_package.dictionary import Dictionary
from python_package.utils import mean_timer

@mean_timer()
def test_insertion_my_class(n=100000):
    my_dict = Dictionary()
    for i in range(n):
        my_dict.add_entry(i, str(i))
    assert(my_dict.num_entries == n)

@mean_timer()
def test_insertion_builtin(n=100000):
    my_dict = {}
    for i in range(n):
        my_dict[i]= str(i)
    assert(len(my_dict) == n)