try:
    f = open('/Users/myh/Desktop/软件破解说明.rtf')
    # print(f.read())
finally:
    if f:
        f.close()


print('---------------')
# with open('/Users/myh/Desktop/PHP/flyAway/CMakeLists.txt',encoding='utf-8') as f:
#     print(f.read())

with open('/Users/myh/Desktop/CMakeLists.txt','w',encoding='utf-8') as r:
    # print(r.read())
    r.write('你好啊！World！')