import random
import string
#优惠码格式为随机字母加数字的组合
selectWord = string.ascii_letters + "0123456789"
#创建优惠码列表
codes = []
# num优惠码数量，length优惠码长度
def code_gen(num, length):
    while len(codes) < num:
        code = ""
        for y in range(length):
            code += random.choice(selectWord)
        if code not in codes:
            codes.append(code)

if __name__ == '__main__':
    code_gen(200, 20) #200个长度为20的优惠码
    print(codes)
