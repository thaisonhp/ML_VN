
import string
from collections import Counter
# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312

def get_top_words(filename, top_n=100):
    # Đọc toàn bộ nội dung của file
    with open(filename, 'r') as file:
        text = file.read()

    # Xóa các ký tự dấu câu và chuyển văn bản thành chữ thường
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    # Chia văn bản thành các từ
    words = text.split()

    # Đếm số lần xuất hiện của từng từ
    word_counts = Counter(words)

    # Lấy 100 từ xuất hiện nhiều nhất
    top_words = word_counts.most_common(top_n)

    # In ra các từ và số lần xuất hiện của chúng
    for word, count in top_words:
        print(f'{word}: {count}')

# Gọi hàm với tên file story.txt
get_top_words('story.txt')
