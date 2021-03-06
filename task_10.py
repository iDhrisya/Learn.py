# -*- coding: utf-8 -*-
"""TASK 10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1di7NemKPuSKP5BRUV7c_aWPgVX3IQXwM

1. Generate two  3 x 3 matrix and find it's dot product and take the transpose of the answer.
"""

import numpy as np
matrix1 = np.random.randint(0,10,(3,3))
matrix2 = np.random.randint(0,10,(3,3))

print(matrix1)
print(matrix2)

dot = np.dot(matrix1,matrix2)
print(dot)

"""2. Create a 3x3 matrix with elements [55,25,15], [30,44,2], [11,45,77] . Now find the determinant of the given matrix."""

import numpy as np
matrix = [[55,25,15],[30,44,2],[11,45,77]]
print(matrix)
det = np.linalg.det(matrix)
print(det)