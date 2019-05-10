from  datetime import datetime

now = datetime.now()
print(now)
print('\n\n')

# 时间转时间戳 转换为秒的时间戳
dt = now.timestamp()
print(dt)
print('\n\n')


# 时间戳转时间
getTime = datetime.fromtimestamp(dt)
print(getTime)
print('\n\n')

# str转为时间戳
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)


# date转时间戳
now = datetime.now()
str = now.strftime('%a, %b %d %H:%M')
print(str)
