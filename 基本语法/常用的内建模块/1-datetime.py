
import time
now = time.time()
now1 = time.localtime(now)
now2 = time.strftime('%Y-%m-%d %H:%M:%S',now1)
print('now = ',now)
print('now1 = ',now1)
print('now2 = ',now2)


# 如果文件命名为datetime.py,这样导入就会报错
# datetime是Python处理日期和时间的标准库。
from  datetime import datetime ,timedelta

dateNow = datetime.now()
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
dateTimeStamp =  dateNow.timestamp()
print('dateNow = ',dateNow)
print('dt = ',dt)
print(dateTimeStamp) #注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
#某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
print(datetime.fromtimestamp(dateTimeStamp))


# str转换为datetime
# 时间的格式可以参考文档
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)


# datetime转换为str
print(dateNow.strftime('%a, %b %d %H:%M'))


# datetime加减
# 需要导入timedelta这个类

print(dateNow + timedelta(hours=10))
print(dateNow + timedelta(days=10))
print(dateNow + timedelta(seconds=10000))
print(dateNow + timedelta(minutes=70))


print(dateNow - timedelta(hours=10))
print(dateNow - timedelta(days=10))
print(dateNow - timedelta(seconds=10000))
print(dateNow - timedelta(minutes=70))