def fact(n = 1):
    if n == 1:
        return 1
    return  n * fact(n-1)

print(fact(980))


#尾递归优化
def fact1(n=1):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num == 1:
        return  product
    return  fact_iter(num - 1, num * product)

print(fact1(980))


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')