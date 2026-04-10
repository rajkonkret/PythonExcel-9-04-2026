# Powerful N-dimensional arrays
# Fast and versatile, the NumPy vectorization, indexing,
# and broadcasting concepts are the de-facto standards of array computing today.

import math

import numpy as np

# pip install numpy

# ndarray - tblice, macierze

array = np.array([10, 100, 1000.])
print(array)  # [  10.  100. 1000.]
print(array.dtype)  # float64

array2 = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(array2)
# [[1 2 3]
#  [4 5 6]]

print(array2.dtype)  # int64

# rzutowanie na typy pythonowe
print(float(array[0]))  # 10.0
print(type(float(array[0])))  # <class 'float'>
