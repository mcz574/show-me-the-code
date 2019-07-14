import random
import string
from random import choice
import pymysql.cursors
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

def save_to_mysql():
    #连接数据库并设置游标
    connect = pymysql.connect('localhost', 'root', '123456', 'db1')
    cursor = connect.cursor()
    #调用命令写入数据(使用replace，存在则覆盖，不存在则插入)
    for i in range(len(codes)):
        write = "replace into `table1` SET `id`='%d', `code`='%s' "%(i+1, codes[i])
        cursor.execute(write)
    #顺便输出一下表中数据
    cursor.execute('select * from table1;')
    data = cursor.fetchall()
    print(tabulate(data, headers=['id', 'code'], tablefmt='psql'))
    #关闭连接
    cursor.close()
    connect.commit()
    connect.close()

if __name__ == '__main__':
    code_gen(200, 20) #200个长度为20的优惠码
    save_to_mysql()
