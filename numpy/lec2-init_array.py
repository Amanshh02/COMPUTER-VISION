import numpy as np

# all 0s matrix
a = np.zeros(5)
print(a,"\n")

#more complex shape- add a () with every increase in dimension
a = np.zeros((5,5))
print(a)

# all one's
a = np.ones((4,2,2))
print(a)

#any other number np.full( (size), value, dtype )
a = np.full( (2,2) , 10 )
print(a)

# full like - take a shape that is already built
a = np.full_like(a , 4)
print(a)

# initialise a matrix number

#decimal
a = np.random.rand(4,2)
print(a)

# integer
a = np.random.randint(low=0, high=100, size=(3, 3))
print(a)

# identity matrix
a = np.identity(3)
print(a)

# repeat array
arr = np.array([1,2,3])
r1 = np.repeat(arr,3)
print(r1)

# solution
output = np.ones((5,5))
print(output)

zero = np.zeros((3,3))

zero[1,1] = 9
print(zero)

output[1:4,1:4] = zero
print("\n",output)

#copying (Be careful!)
a = np.array([1,2,3])
# b = a # now changes made to any of them will reflect on the other one :(
# b[0] = 100 # changes value of both a and b

b = a.copy()
b[0] = 100

# basic arithemetics can be done on every element at once 

#trigonometry
print(np.sin(a))
