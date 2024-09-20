# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]
import numpy as  np 
def check_element(data1:np.array , data2:np.array):
    result = []
    for i in data1 : 
        if i in data2 : 
            result.append(i)    
    return result 

# cach 2 
def check_element_v2(data1: np.array, data2: np.array) -> np.array:
    return data1[np.isin(data1, data2)]

Array1 = np.array([0,10 ,20, 40, 60])
Array2 = np.array([10, 30, 40])
result = check_element_v2(Array1,Array2)
print(result)