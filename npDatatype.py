import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr1 = np.array([1, 2, 3, 4], dtype='i4')

print(arr1)
print(arr1.dtype)

arr2 = np.array([1, 2, 3, 4], dtype='i8')

print(arr2)
print(arr2.dtype)

arr3 = np.array([1.1, 2.1, 3.1])

newarr = arr3.astype('i')

print(newarr)
print(newarr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)