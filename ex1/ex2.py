# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# loại bỏ các phần tử trùng lặp 
data_processed = list(set(data2))
k = 3
# kiểm tra điều kiện 
result = [data_processed[i] for i in range(len(data_processed)) if data2.count(data_processed[i]) > 3]
print(result)