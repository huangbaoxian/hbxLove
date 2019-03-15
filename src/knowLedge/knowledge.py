# 字符串 可以用'''___'''标识多行类型
str = '''love python 
really
result'''
print(str)

print('\n\n')
# 布尔值
# 可以用and计算
# or 运算
# not 非运算

l = True
k = False

if l :
    print('l is ture')
else:
    print('l is false')

if k :
    print('k is true')
else:
    print('k is false')

if k and l :
    print('k and l is true')
elif l and (not k):
    print('l is ture and k is false')
else:
    print('k is false or l is false')
print('\n\n')
# 空值
n = None
print(n)

print('\n\n')
#字符串
#获取字符整数标识
print(ord('A'))#65
print(ord('中'))#20013
print(chr(66))#B
print('\n\n')

# 字符编码
a1 = 'ABC'.encode('ascii')
b1 = '中文'.encode('utf-8')
print(a1)
print(b1)
a1 = a1.decode('ascii')
b1 = b1.decode('utf-8')
print(a1)
print(b1)
print('\n\n')

# 字符串拼接
a2 = 'ABC'
b2 = 'DEF'
print(' %s %s' %(a2, b2))
print('\n\n')


# 列表
student = ['1', 2, '3']
print(student)
print(student[0])
print(len(student))
# 获取最后一个元素
print('最后一个元素%s' %(student[-1]))
student.insert(1, '4')
print('插入元素之后%s'%student)
student.pop(1)
print('删除一个指定位置的元素%s'%student)
student.pop()
print('删除最后一个元素%s'%student)
student[1] = 'student'
print('元素替换%s'%student)
print('\n\n')



# 不变的数组 元组
classmate = ('student1','student2','student3')
print(classmate)
# 定义一个元素的时候必须加上逗号
classmate1 = (1,)
print(classmate1)
classmate2 = (1)
print(classmate2)
# 如果元组里面有list，则list长度可以发生变化
print('\n\n')

# 逻辑判断
# brith = input()
# brith = int(brith)
# if brith < 200 :
#     print('hello world')
# else:
#     print('my class')
# print('\n\n')


# 循环逻辑
# for in    while
names = ['a','b','c']
name = ''
for n in names :
    name = ('%s%s'%(name,n))
    # name.__add__(n)
print(name)
print('\n\n')


countList = list(range(5))
tmp = 0
for x in countList:
    tmp += x
print(tmp)
print('\n\n')



#字典 dict set
# 字典找不到会报错
# dict
company = {'1':1, '2':2}
# 第一种方式
if '2' in company:
    print(company['2'])

# 使用get方式获取值
print(company.get('1'))
# 删除key用pop()方法
print('\n\n')


# set 元素
s = set([1,2, 3, 4, 5])
print(s)
s.add(5)
print(s)
s.remove(4)
print(s)
print('\n\n')



# 定义函数

def my_abs(x):
    if x > 0:
        return x
    else:
        return  -x
print(my_abs(-100))

# 空函数  使用pass  pass可以当做占位符
def nop():
    pass
# 检测数据类型
print(isinstance(1, (int)))
print('\n\n')



#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(10))
print('\n\n')



print('init', 4)
print('\n\n')


# 函数式调用
r = []
n = 3
for i in range(n):
    r.append(i)
print(r)







print('\n\n')
l = ['1', '2', '3', '4', '5','6','7','8','9','10']
# 切片应用
# 获取数据前三个数据
index = 2
if l >  l:
    print(l[0:index]);
else:
    print(l[0:2]);

print(l[0:3])
print(l[1:4])
print(l[3:4])
# 每几个取几个 每4个取2个
print('每4个取2个')
print(l[:4:2])
# 没2个取1个
print('每2个取一个')
print(l[::4])

# 复制一个列表
print(l[:])
# 字符串也支持
kstr = 'ajksdhjkashdjkashd'
print(kstr[0:3])











