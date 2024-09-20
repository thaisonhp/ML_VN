import numpy as np 
# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]

data = np.array([1,6,4,8,9,-4,-2,11])
max = np.argmax(data)
min = np.argmin(data)
print(max,min)