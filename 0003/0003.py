import redis
import random
import string
from tabulate import tabulate

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

def save_to_redis():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for i in range(len(codes)):
        r.set(i+1,codes[i])
    #顺便打印一下数据库中的键值对
    keys = r.keys('*')
    for key in keys:
        print(key, ':' ,r.get(key)) 
        #这里输出的是byte，不是字符串，格式也比较简陋，有时间再搞

if __name__ == '__main__':
    code_gen(200, 20) #200个长度为20的优惠码
    save_to_redis()
    