# 函数的参数类型
# 加
def add(x, y):
    return x + y

# 减
def subtract(x, y):
    return x - y

# 乘
def multiply(x, y):
    return x * y

# 除
def divide(x, y):
    return x / y

# 计算
def calc(x, y, oper):
    return oper(x, y)
print(calc(10, 20, add))


# 匿名函数
# 需求1: 打印一个分割线
out_line = lambda: print("-----------------------------------")
out_line()

# 计算两个数之和
add = lambda x, y: x + y
print(add(10, 20))

# 需求3: 完成如下列表的排序操作, 按照每一个元素的字符个数, 从小到大排序
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]

data_list.sort(key=lambda item: len(item), reverse=True) # 匿名函数典型的应用场景
print(data_list)






