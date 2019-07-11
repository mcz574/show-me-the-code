import random
import string

selectWord = string.ascii_letters + "0123456789"
codes = []

def code_gen(count, length):
    while len(codes) < count:
        code = ""
        for y in range(length):
            code += random.choice(selectWord)
        if code not in codes:
            codes.append(code)

if __name__ == '__main__':
    code_gen(10, 20)
    print(codes)
