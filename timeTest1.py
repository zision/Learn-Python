import time

print(time.time())  # 从1970年1月1日午夜至今的时间

print(time.localtime())  # 当前时间信息

print(time.mktime(time.localtime()))  # 转为时间戳

t = time.mktime(time.localtime())
print(time.asctime(time.localtime()))  # 转换为一般容易识别的时间形式
print(time.ctime(t))  # 将时间戳转换为容易识别的时间形式

a = time.strftime('%Y-%m-%d %X', time.localtime())
print(a)
# 自行设定输出字符串的格式

print(time.strptime('2018-01-06 22:46:24', '%Y-%m-%d %X'))
# 逆向操作


time.sleep(3)  # 先休息3秒
for i in range(1, 10):
    print(i)
    time.sleep(1)
    # 每隔一秒打印一次

