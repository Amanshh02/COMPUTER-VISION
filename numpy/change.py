import numpy as np

# accessing and elements of an array

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# get a specific element
print(a[1,5])
print(a[1,-2])

# get a specific row
print("slice",a[0, :]) # slice method :
print(a[:,3])

#[startindex:endindex:stepsize]
print(a[0, 1:6:2])


# CHANGING

print('\n')
a[1,5]= 20
print(a)
print('\n')
a[: , 2] = [1,2]
print(a)
print('\n')
#3d
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#get specific element (work outside in)
print(b[0,1,1])

# replace
print(b[: , 1 , :])
