import numpy as np

# a = [1,2,3,4,5] is a list

# initialisation

# 1d
a = np.array([1,2,3], dtype='int16')
print(a)

# 2d
b= np.array([[1,2,3,4,5], [6,7,8,9,0]])
print(b)

# get dimension
print("Dimension is (rows) : ", b.ndim)

#shape
print("Shape is (matrix shape) : ", b.shape) #shape of matrix

# get type
print("Data type is : ", a.dtype)

# get size
print(" Size of one item is : ", a.itemsize)

# get total size
print("Size (no. of elements) : ", b.size)
print("Size in bytes : ", a.nbytes)

