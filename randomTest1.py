# random模块
import random
print(random.random())  # 生成0到1随机浮点数
print(random.uniform(1, 100))  # 生成指定范围内随机浮点数
print(random.randint(1, 100))  # 生成指定范围内随机整数
print(random.randrange(10, 100, 2))  # 从指定序列中获取一个随机数

print(random.choice('Py大法好！'))  # 随机选取
print(random.choice(('a', 'b', 'c')))  # 可以是字符串，元组，列表等

list1 = [1, 2, 3, 4, 5, 6]
random.shuffle(list1)  # 将列表中元素打乱（洗牌）
print(list1)

list2 = [i**2 for i in range(0, 10)]
print(list2)
print(random.sample(list2, 3))  # 随机获取指定数量的片段
print(list2)  # 不会修改原有列表

