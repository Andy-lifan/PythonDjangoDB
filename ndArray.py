#!/usr/bin/env python3

import numpy as np

arr = np.array([[1, 2, 3, 4, 5],[10,11,12,13,14]])

print(arr[0:2,2:4])

arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd dim: ', arr1[1, 4])

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr2[0, 1, 2])

arr3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr3[1, -1])

arr4 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr4[-3:-1])

arr5 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr5[1:5:2])

arr6 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr6[1, 1:4])

arr7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr7[0:2, 2])

arr8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr8[0:2, 1:4])