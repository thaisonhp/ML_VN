# # Ex4: print all Possible Combinations from the three Digits
# data4 = [1, 2, 3]



# def view_config(x:list):
#     print(x[1:])


# def next_config(x, i):
#     # Hàm tạo cấu hình tiếp theo
#     n = len(x) - 1
#     k = n
#     while x[i] > x[k]:
#         k -= 1
#     x[i], x[k] = x[k], x[i]
#     j, r = i + 1, n
#     while j < r:
#         x[j], x[r] = x[r], x[j]
#         j += 1
#         r -= 1

# def listing_configs(elements):
#     x = [0] + elements[:]  # Thêm một phần tử 0 ở đầu danh sách
#     n = len(elements)
#     i = n - 1

#     while True:
#         view_config(x)  # In một cấu hình
#         # Tìm phần tử liền trước đoạn cuối giảm dần
#         while i > 0 and x[i] > x[i + 1]:
#             i -= 1
#         if i == 0:
#             break  # Đã đến cấu hình cuối cùng
#         next_config(x, i)
#         i = n - 1


# listing_configs(data4)

from itertools import permutations
# permutations là để sinh ra các hoán vị của 1 list 
data4 = [1, 2, 3]

def print_all_combinations(data):
    all_combinations = list(permutations(data))
    for combination in all_combinations:
        print(combination)

print_all_combinations(data4)
