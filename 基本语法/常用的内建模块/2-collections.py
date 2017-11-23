from collections import  namedtuple
##############      namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
point = namedtuple('Point',['x','y','z'])
p = point(1,2,3)
print(p.x,p.y,p.z)
print(isinstance(p,point))
print(isinstance(p,tuple))


from  collections import deque
##### ##########  deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q.insert(2,'z')
q.appendleft('m')
print(q)


from collections import defaultdict
###############   defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict
# 如果要保持Key的顺序，可以用OrderedDict：
ddd = dict([('a', 1), ('b', 2), ('c', 3)])
ddd1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ddd)
print(ddd1)