# 打开文本文件
with open("./0004/English.txt", 'r') as f:
    words = f.read()

# 使用空格进行分词，存到列表里
words_list = words.split(' ')

# print(words_list)
# 虽然分词后仍然有逗号句号等特殊符号，但会和单词连在一起，不影响单词数量的统计
# 学一下正则表达式后再更新

print(len(words_list))