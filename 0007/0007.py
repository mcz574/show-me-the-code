# https://blog.csdn.net/huangxiongbiao/article/details/45505425
#coding: utf-8
import os, re

# 代码所在目录
FILE_PATH = './0007/codes_files'

def analyze_code(codefilesource):
    '''
    打开一个py文件，统计其中的代码行数，包括空行和注释
    返回含该文件总行数，注释行数，空行数的列表
    '''
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(codefilesource) as f:
        lines = f.readlines()
        total_line = len(lines)
        line_index = 0
        # 遍历每一行
        while line_index < total_line:
            line = lines[line_index]
            # 检查是否为注释
            if line.startswith("#"):
                comment_line += 1
            elif re.match("\s*'''", line) is not None:
                comment_line += 1
                while re.match(".*'''$", line) is None:
                    line = lines[line_index]
                    comment_line += 1
                    line_index += 1
            # 检查是否为空行
            elif line == "\n":
                blank_line += 1
            line_index += 1
    print("在%s中：" % codefilesource)
    print("代码行数：", total_line)
    print("注释行数：", comment_line)
    print("空行数：  ", blank_line)
    return [total_line, comment_line, blank_line]


def run(FILE_PATH):
    # 切换到code所在目录
    os.chdir(FILE_PATH)
    # 遍历该目录下的py文件
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.py':
            line = analyze_code(i)
            total_lines, total_comment_lines, total_blank_lines = total_lines + line[0], total_comment_lines + line[1], total_blank_lines + line[2]
    print("总代码行数：", total_lines)
    print("总注释行数：", total_comment_lines)
    print("总空行数：  ", total_blank_lines)

if __name__ == '__main__':
    run(FILE_PATH)