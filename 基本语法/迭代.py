from  collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)

# 判断一个对象是否可以迭代呢
print(isinstance(123,Iterable),isinstance('123123',Iterable))

# list实现类似其他语言的迭代
for i, value in enumerate(['ASAS','jkahsda',['ada','adadas']]):
    print(i,value)

for x,y,z in [(1,2,3),(4,5,6),(7,8,9)] :
    print(x,y,z)

def findMinAndMax(L):
    if L.count == 0:
        return (None,None)
    x = L[0]
    y = L[0]
    for value in L:
        if x > value:
            x = value
        if y<value:
            y = value
    return (x,y)

print(findMinAndMax([7, 1, 3, 9, 5]))