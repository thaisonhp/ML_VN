# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient

f = open("/Users/luongthaison/Documents/Third_years_student/ML_basic_VietNguyen/ex1/wordsEn.txt")
f = list(i[0:len(i)-1] for i in f)
# f = list(i for i in f)
# print(f)
