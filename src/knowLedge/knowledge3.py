
# 读取文件#
# with open('/Users/huangbaoxian/Desktop/test/te', 'r') as f:
#     print(f.read())



# # 读取文件2
# with open('/Users/huangbaoxian/Desktop/test/te', 'r') as f:
#      fileList = f.readlines()
#      i = 0
#      for index in fileList:
#          i = i + 1
#          print(i)
#          print(index)




# 写入文件
with open('/Users/huangbaoxian/Desktop/test/te', 'w') as f:
     i = 0
     while i < 10:
         i = i + 1;
         f.write('hello world')

