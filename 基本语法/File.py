import os
import shutil
# def file_name(file_dir):
#     # os.listdir('./')
#     # walk
#     roots = [d for d in os.listdir(file_dir) if d != '.DS_Store']
#     print('roots = ',roots)
#     subRoots = []
#     for root in roots:
#         #在这里我们去记录我们的文件夹路径
#         roots1 =  [d for d in os.listdir(file_dir + '/' + root) if d != '.DS_Store']
#         subRoots.append(roots1)
#         print('roots1 = ',roots1)
#
#     print('subRoots = ',subRoots)
#     removeValue = []
#     for i,value in enumerate(roots):
#         for j,subValue in enumerate(subRoots[i]):
#             subValueStr = file_dir + '/' + value + '/' + subValue
#             removeValue.append(subValueStr)
#             #在这里，我们开始移动
#             subSubRoots = [d for d in os.listdir(subValueStr) if d != '.DS_Store']
#             print('subSubRoots = ', subSubRoots)
#             for subSubValue in subSubRoots:
#                 subSubRootsStr = file_dir + '/' + value + '/' + subValue + '/' + subSubValue
#                 shutil.move(subSubRootsStr, file_dir + '/' + value + '/' + subSubValue)
#                 print('subSubRootsStr = ', subSubRootsStr)
#     print(removeValue)
#     for value in removeValue:
#          shutil.rmtree(value)
#
#     print(os.walk(file_dir))

# file_name('/Users/myh/PycharmProjects/PythonFirst/视频')
# file_name('/Users/myh/Desktop/PHP')

# shutil.move('/Users/myh/Desktop/SVN', '/Volumes/H/BaiduNetdiskDownload/SVN')