"""
here we will discover the numpy library
"""

# Imports
import numpy as np
from utils import timer


# Functions

def numpy_sum(my_array: np.array):
    return my_array.sum()

def random_array(rows: int, cols: int):
    return np.random.rand(rows, cols)

def random_symmetric_array(size: int):
    matrix = np.random.rand(size, size)
    return (matrix + matrix.T)/2

def random_semi_definite_array(size: int):
    matrix = np.random.rand(size, size)
    return matrix@matrix.T

def diagonlisation(my_array: np.array):
    assert(np.linalg.det(my_array) != 0)
    valp, vecp = np.linalg.eig(my_array)
    D = np.diag(valp)
    return vecp, D, np.linalg.inv(vecp)

@timer
def resol(my_array: np.array, b: np.array):
    assert(np.linalg.det(my_array) != 0)
    return np.linalg.inv(my_array)@b
@timer
def resol_cholesky(my_array: np.array, b: np.array):
    assert(np.linalg.det(my_array) != 0)
    assert(np.all(my_array == my_array.T))
    assert(np.all(np.linalg.eigvals(my_array) > 0))
    L = np.linalg.cholesky(my_array)
    return np.linalg.inv(L.T)@np.linalg.inv(L)@b
@timer
def resol_qr(my_array: np.array, b: np.array):
    assert(np.linalg.det(my_array) != 0)
    Q, R = np.linalg.qr(my_array)
    # return np.linalg.inv(R)@Q.T@b
    return np.linalg.solve(R, Q.T@b)
@timer
def resol_builtin(my_array: np.array, b: np.array):
    assert(np.linalg.det(my_array) != 0)
    return np.linalg.solve(my_array, b)
@timer
def resol_lstsq(my_array: np.array, b: np.array):
    assert(np.linalg.det(my_array) != 0)
    return np.linalg.lstsq(my_array, b, rcond=None)


# Main
def main():
    my_array = random_semi_definite_array(1000)
    # U, D, U_1 = diagonlisation(my_array)
    # approx = U@D@U_1
    # print(np.allclose(my_array, approx))
    # print(my_array-approx)

    b = np.random.rand(1000)
    resol(my_array, b)
    resol_cholesky(my_array, b)
    resol_qr(my_array, b)
    resol_builtin(my_array, b)
    resol_lstsq(my_array, b)
if __name__=="__main__":
    main()