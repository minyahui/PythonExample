import psutil
print('CPU逻辑数量 = ',psutil.cpu_count())
print('CPU物理核心 = ',psutil.cpu_count(logical=False))
print('统计CPU的用户／系统／空闲时间 = ',psutil.cpu_times())
print('获取内存信息 = ',psutil.virtual_memory())
print('获取内存信息 = ',psutil.swap_memory())
print('磁盘分区信息 = ',psutil.disk_partitions())
print('磁盘使用情况 = ',psutil.disk_usage('/'))

print('磁盘IO = ',psutil.disk_io_counters())
print('获取网络读写字节／包的个数 = ',psutil.net_io_counters())
print('获取网络接口信息 = ',psutil.net_if_addrs())
print('获取网络接口状态 = ',psutil.net_if_stats())

# print('获取当前网络连接信息 = ',psutil.net_connections())
