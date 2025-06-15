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
print(a.ndim)

#shape
print(b.shape)

# get type
print(a.dtype)

# get size
print(a.itemsize)

# get total size
print(a.size)
print(a.nbytes)

