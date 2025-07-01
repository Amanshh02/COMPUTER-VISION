import numpy as np

# Linear Algebra
a = np.ones((2,3))
print(a)

b= np.full((3,2),2)
print(b)

# a*b is an error

#multiplication
print(np.matmul(a,b))

#determinant
c = np.identity(3)
print(np.linalg.det(c))

