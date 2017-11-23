def my_abs(x):
    if x >= 0:
        return  x
    else:
        return -x

print (my_abs(-99))

def power(x,n = 1):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print (power(5,2),power(5))


def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print (add_end())
print (add_end(['x','y']),add_end(),add_end(),add_end())
# 可变参数
def calc(*numbers):
    msum = 0
    for n in numbers:
        msum = msum +  n * n
    return msum

print (calc(1,2,3),calc(10,2,39,90),calc())
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print ('name:',name, 'age:',age, 'other:',kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Michael',30)
person('Michael',40,city='beijing')
person('Michael',50,city='beijing',job='iOS')
person('Michael',60,**extra)

# 命名关键字参数
def person1(name, age,*, job='iOS', city='WuHan'):
    print (name, age, job, city)
person1('Minyahui',24,)
person1('YeHuan',24,job='Web')
person1('XiaoWei',24,city='BeiJing')

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2, 3, 'a', '你好')
f1(1, 2, 3, 'a', 'b', x=99)

def product(*proNumber):
    pro = 1
    for i in proNumber:
        pro = pro * i
    return  pro

print(product(1),product(2,3,4),product(4,9,20))