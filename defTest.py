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


# 字典类型的变长度参数传递
def da_yin3(a, *b, **c):
    # 参数前加两个星号*，表示可变长度字典
    print(a, b, c)


print('')
da_yin3(1, 2, 3, q=4)
da_yin3(1)


# 实现不带括号的字典类型变长度参数传递打印
def da_yin0(a, *b, **c):
    print(a, end='')
    print(' ', end='')
    if len(b) is not 0:
        for i in b:
            print(i, end='')
            print(' ', end='')
    if len(c) is not 0:
        for j in c:
            print(c[j], end='')
            # c[j]指打印j键对应的值，否则如haha=80会打印出haha
            print(' ', end='')
    print('')


da_yin0(1, 2, 3)
da_yin0(1, 2, 3, 4, 5, 6, 7, haha=80)
da_yin0(1, 2, haha=80, 4, 5, hehe=70)
# 可变参数需要写在最后，顺序不能错，否则报错