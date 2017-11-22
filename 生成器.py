g = (x * x for x in range(1, 11))
print(g)
for n in g:
    print(n)
# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(10)

def triangles(n):
    L = [1]  # 定义一个list[1]
    print(L)
    if len(L) >= n:  # 仅输出10行
        return
    while True:
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]  # 计算下一行中间的值（除去两边的1）
        L.insert(0, 1)  # 在开头插入1
        L.append(1)  # 在结尾添加1
        print(L)
        if len(L) > n:  # 仅输出10行
            break

triangles(16)
