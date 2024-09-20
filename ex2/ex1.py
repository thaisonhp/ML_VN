import numpy as np 
import pandas as pd 


# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
def reverse_np(data:np.array) -> np.array:
    return data[-1::-1]
 

data = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
data_new = np.array(data)
# cach 1 
# data_pred = reverse_np(data_new)
# cach 2 : 
data_pred = np.flip(data_new)
print(data_pred)







