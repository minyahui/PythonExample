print(list(range(1, 11)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

def lower(L):
    L1 = [s.lower() for s in L if isinstance(s,str)]
    return L1
print(lower(['Hello', 'World', 18, 'Apple', None]))
print(lower(['HELLO', 'WOrld', 18, 'Apple', None,['hahhs','hjahsaj']]))


import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('./')]) # os.listdir可以列出文件和目录