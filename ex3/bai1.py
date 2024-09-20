import gensim.downloader as api
import numpy as np

# 25, 50, 100 or 200. Số càng lớn thì càng chính xác, nhưng chạy càng lâu các bạn nhé
#Tải mô hình GloVe:
model = api.load("glove-twitter-200")
# word = "beautiful"
# # print(model[word])
# # In vector từ:
# print("1----------")
# result = model.most_similar(word, topn=10)
# print(result)
# # # Tìm các từ tương đồng nhất với một từ
# # print("2----------")
# # result = model.most_similar(positive=["january", "february"], topn=10)
# # print(result)
# # # Tính độ tương đồng giữa hai từ
# # print("3----------")
# # result = model.similarity("man", "woman")
# # print(result)
# # # Tìm từ tương đồng nhất khi trừ đi vector của một từ
# # print("4----------")
# # result = model.most_similar(positive=["woman", "king"], negative=["man"], topn=1)
# # print(result)
# # # Tính độ tương đồng giữa "berlin" và "vietnam", khi trừ đi "hanoi" 
# # print("5----------")
# # result = model.most_similar(positive=["berlin", "vietnam"], negative=["hanoi"], topn=1)
# # print(result)
# # Tính độ tương đồng giữa "marriage" và "happiness":
# print("6----------")
# result = model.similarity("marriage", "happiness")
# print(result)


#TODO: Các bạn thử viết 2 cách khác nhau để tính cosine similarity
# giữa 2 vector nhé. Kết quả giống với khi dùng model.similarity() là được
# 1 cách là dùng numpy, 1 cách là không dùng numpy nhé
import numpy as np

def cosine_similarity_numpy(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

vec1 = model["man"]
vec2 = model["wman"]
print(cosine_similarity_numpy(vec1, vec2))
# print(type(model["marriage"]))
import math

def cosine_similarity_no_numpy(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm_vec1 = math.sqrt(sum(a * a for a in vec1))
    norm_vec2 = math.sqrt(sum(a * a for a in vec2))
    return dot_product / (norm_vec1 * norm_vec2)


