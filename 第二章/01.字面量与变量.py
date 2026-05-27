# 字面量的写法
from platform import python_implementation

print(100)
print(3.14)
print(True)
print(False)
print("Hello Python")
print("----------------------")
print(None)

# 布尔类型本质也是数字类型(True - 1;False - 0 )
print(True + 1)
print(False - 1)

# 变量
num = 1114.1
print(num)

num = num + 1
print(num)

base,incr = 20.7,50
print("第一个月播放总量: ",base + incr)
print("前两个月播放总量: ",base + incr*2)

name = "python"
print(name)

a = 100
b = 200
c = 300
x = c
c = a
a = b
b = x
print(a,b,c)






