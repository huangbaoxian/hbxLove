import  os
from functools import reduce
from operator import itemgetter
import functools


#列表上传  前闭后开
print(list(range(2, 30)))
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]


# [1x1, 2x2, 3x3, ..., 10x10]
print('\n\n')
listX = [x * x for x in range(1, 11)]
print(listX)

print('\n\n')
#双层循环创建数据
listY = [m + n for m in 'ABC' for n in 'XYZ']
print(listY)


# 获取文件夹下面所有文件名称

print('\n\n')
path = '/Users/huangbaoxian/Documents/webSpace'
listF = [d for d in os.listdir(path)]
print(listF)
print('\n\n')

# 生成器  生产的数据为()
g = (x * x for x in range(10))
for n in g:
    print(n)



print('\n\n')
# 高阶函数  map reduce
def f(x):
    return x *x

r = map(f, [1,2,3,4,5,6,7,8,9])

listK = list(r)
print(listK)
print('\n\n')

# reduce的累积作用
def add(x,y):
    return  x + y
re = reduce(add, [1,3,5,7,9])
print('reduce result is ', re)
print('\n\n')
def fn(x,y):
    return x* 10 + y
fns = reduce(fn, [1,3,5,7,9])
print('fns result is',fns)

# 将字符转化为数组
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print('string to int value', str2int('45678'))


# filter 过滤函数 实现筛选功能
def is_odd(x):
    return x%2==1

filter1 =  list(filter(is_odd, [1,2,3,4,5,6,7,8,9 ]))
print('filter list is ', filter1)
print('\n\n')


# sorted排序函数
sortedList = [1, 90, -20, 33,25]
print(sorted(sortedList))
# 接收函数
print(sorted(sortedList, key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 逆序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 测验，班级成绩排名
grade1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(grade1, key=itemgetter(1)))
print('\n\n')



# 函数当成返回值

# def lazy_sum(x):
#     def sumX():
#         ax = 0
#         for i in x:
#             ax+=i
#         return  ax
#     return sumX
#
# f = lazy_sum(10)
# print('f is',  f)
# print('f_result is ' ,f())

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# newFx = lazy_sum([1,3,5,6,7])
# print('new Fx result is', newFx())


# 匿名函数  关键字lambda表示匿名函数，冒号前面的x表示函数参数。
newList1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print('newlist1 is :', newList1)
print('\n\n')


# 函数也是变量
def now():
    print('2018-03-18')
    return  20
fnow = now
print('fnow run is ', fnow(), '  fnow name is: ', fnow.__name__ , ' fnow dict is ',fnow.__dict__)


# 装饰器  类似java的切片， iOS的runtime， 修改函数的功能，但是不改变原函数的功能
# 简单的log功能
def log(fun):
    def warpper(*args, **argv):
        print('call ' , fun.__name__)
        return fun(*args, **argv)
    return warpper
print('\n\n')


@log
def action1():
    print('123')

action1()

# 带参数的log功能更
def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log1('execute')
def action2():
    print('456')
action2()



# 通用log打印 带参数和不带参数

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

print('\n\n')

# 偏函数
# 在原函数上添加默认参数等设置

# int2 = functools.partial(int, base=2)
# print('16进制34 is:', int2(1000000))
# print('666')



