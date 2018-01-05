list1 = [1,2,3,4,5]
print(list1[0])

list2 = ['a','b','c','d','e','f']
print(list1+list2)

print(list1*3+list2)

print(len(list1),len(list1*3),len(list1+list2))

for i in list1:
    print(i)

print(2 in list1,6 in list1)

del list2[0]
print(list2)

print(max(list2))

#统计某个元素在列表中出现的次数

