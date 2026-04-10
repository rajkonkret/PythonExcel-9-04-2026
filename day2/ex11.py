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

import json

x = np.int64(64)
print(type(x))  # <class 'numpy.int64'>

# serializacja danych - zamina na json
# json.dumps(x) # TypeError: Object of type int64 is not JSON serializable
python_int = int(x)
json_str = json.dumps({"value": python_int})
print(json_str)  # {"value": 64}

# broadcasting
# # [[1 2 3]
# #  [4 5 6]]

print(array2 + 1)
# [[2 3 4]
#  [5 6 7]]

print(array2 + array2)
# [[ 2  4  6]
#  [ 8 10 12]]

print(math.sqrt(25))  # 5.0

# print(math.sqrt(array2))  # TypeError: only 0-dimensional arrays can be converted to Python scalars

# numpy posiada własne metody
print(np.sqrt(array2))
# [[1.         1.41421356 1.73205081]
#  [2.         2.23606798 2.44948974]]

# suma elementów tablice
print(array2.sum())  # 21
