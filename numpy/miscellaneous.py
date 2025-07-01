import numpy as np

# Step 1: Create and save the file
data = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
np.savetxt("data.txt", data, delimiter=",", fmt="%d")

# Step 2: Now load it
file_data = np.genfromtxt('data.txt', delimiter=',')
print(file_data)
