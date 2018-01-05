# 尝试一般的加法定义
def jia_fa(a,b):
    return a + b


print(jia_fa(3, 4))

# 尝试默认减2的减法定义


def jian_fa(a, b=2):
    # 定义一个加法
    return a - b


print(jian_fa(4))

# 元组类型的变长度参数传递


def da_yin1(a, *b):
    print(a, b)


da_yin1(1, 2, 3, 4)

# 试试没有括号的


def da_yin2(a, *b):
    print(a, end='')
    print(' ', end='')
    for i in b:
        print(i, end='')
        print(' ', end='')


da_yin2(1, 2, 3, 4, 5, 6, 7, 8, 9)

