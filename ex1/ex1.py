# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
def count(data : list)->list:
    '''
        input : list - danh sách các số 
        hàm tìm số lượng số dương , số âm
        output : (list) gồm 2 phần tử : số lượng số dươn và số lương số âm 
    '''
    result = len([i for i in data if i > 0])
    return [result,len(data)-result]

num_positive , num_negative = count(data1)
print("positive:",num_positive)
print("positive:",num_negative)