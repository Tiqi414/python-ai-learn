# ------------------------------------ 函数 - 变量的作用域------------------------------------

# 全局变量
num = 100

# 定义函数
def circle_area(r):
    # 局部变量: 只能在函数内部使用
    pi = 3.14
    area = pi * r * r
    global num
    num = 10000
    print("num = ", num)
    return area

# 函数调用
c_circle = circle_area(10)
print(c_circle)

print("num = ",num)


# --------------------------- 函数 - 传参方式 ----------------------------
# 定义函数
def reg_stu(name, age, gender, city):
    """
    录入个人信息
    :param name: 姓名
    :param age: 年龄
    :param gender: 性别
    :param city: 城市
    :return: 信息
    """
    print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
    # return name, age, gender, city
    return {"name":name, "age":age, "gender":gender, "city":city}

reg_stu("张三", "18", "男", "上海")

# 传参方式一: 位置参数
stu = reg_stu("张三", "18", "男", "上海")
print(stu)

# 传参方式二: 关键字参数 顺序可以调换
stu = reg_stu(name = "王林", age = "18", gender = "男", city = "上海")
print(stu)

# 传参方式三: 位置参数 + 关键字参数 ---> 位置参数在前, 关键字参数在后
stu = reg_stu( "李慕婉","18", gender = "女", city = "上海")
print(stu)


# --------------------------- 函数 - 默认参数 ----------------------------
# 定义函数
def reg_stu(name, age, gender="男", city="北京"):
    print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
    return {"name":name, "age":age, "gender":gender, "city":city}
stu = reg_stu("王林","18")
print(stu)

stu = reg_stu("李慕婉", "18", "女")
print(stu)

stu = reg_stu("韩立", "18", city="上海")
print(stu)

# --------------------------- 函数 - 不定长参数 (位置参数 *args) ----------------------------
# 需求: 根据传入的这批数据,计算这批数据的最小值，最大值，平均值
def calc_date(*args):
    min_date = min(args)
    max_date = max(args)
    avg_date = sum(args) / len(args)
    return min_date, max_date, round (avg_date,1)

# 调用函数
print(calc_date(2,7,9,10,45))
print(calc_date(2,7,9,10,45,73,37,93,111,92,222))

# --------------------------- 函数 - 不定长参数 (关键字参数 **kwargs) ----------------------------
# 需求: 根据传入的这批数据,计算这批数据的最小值，最大值，平均值
def calc_date(*args, **kwargs):
    """
    根据传入的这批数据,计算这批数据的最小值，最大值，平均值
    :param args: 不定长位置参数, 需要计算的这批数据
    :param kwargs: 不定长关键字参数
        round: 保留的小数个数
        print: 是否打印输出
    :return: 最小值, 最大值, 平均值
    """
    min_date = min(args)
    max_date = max(args)
    avg_date = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_date = round (avg_date,kwargs.get("round"))
    if kwargs.get("print") :
        print(f"计算出来的最小值: {min_date}, 最大值: {max_date}, 平均值: {avg_date}")
    return min_date, max_date,  avg_date

# 调用函数
print(calc_date(2,7,9,10,45,round=3, print=True))
print(calc_date(2,7,9,10,45,73,37,93,111,92,222, round=3, print=False))
