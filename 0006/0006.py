# 最重要的词==出现次数最多的词，涉及到字数统计
# 个人认为有难度，参考https://blog.csdn.net/Jacky_chenjp/article/details/52268272
from collections import Counter
import re
import string
import os

dir = './0006/diary'
except_words = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this','s', 'is', 'are', 'a', 'with', 'as', 'an', 'i', 'my', 'at']

def find_word():
    for txt_file in os.listdir(dir):
        with open(dir + '/' +txt_file, 'r') as f:
            data = f.read().lower()
            #筛选出所有字母和数字
            pat = '[a-z0-9\']+'
            words = re.findall(pat, data)
            wordList = Counter(words)
            for i in except_words:
                wordList[i] = 0
    return wordList.most_common()[0]

if __name__ == "__main__":
    most_important = find_word()
    print(most_important[0],most_important[1])
