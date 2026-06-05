# 定义函数:函数定义的时候并不会执行, 只有在调用函数的时候, 函数的逻辑才会执行; 函数必须先定义, 再调用
# def out_line():
#     print("---------------------------")
#     print("---------------------------")
#
# # 函数调用
# out_line()
import math


# 函数的参数与返回值
# # 函数1: 计算圆的面积 -- 半径
# def circle_area(r):
#     area = 3.14 * r ** 2
#     return area
# area = circle_area(10)
# print(area)
#
# # 函数2: 计算长方形的面积 -- 长, 宽
# def rectangle_area(l,w):
#     """
#     根据长方形的长度和宽度, 计算长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
# # help(rectangle_area)
# print(rectangle_area(10,5))
#
# # 函数3: 计算圆的面积, 周长 -- 半径 ---> 如果返回值有多个, 多个返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
# def circle_area_circum(r):
#     """
#     根据圆的半径, 计算圆的面积和周长
#     :param r: 半径
#     :return: 圆的面积. 圆的周长
#     """
#     return round(3.14 * r ** 2, 1), round(2 * 3.14 * r, 1)
#
# al = circle_area_circum(10)
# print(al)
# print(type(al))
#
# area, circum = al
# print(area)
# print(circum)


# 函数的嵌套调用
# def function_a():
#     print("a ... before")
#     function_b()
#     print("a ... after")
#
# def function_b():
#     print("b ... before")
#     function_c()
#     print("b ... after")
#
# def function_c():
#     print("c ...")
#
# function_a()
#
# print("函数调用完毕 ~")


# 案例:
# 需求1: 定义一个函数: 根据传入的低和高计算三角形面积的函数 (三角形面积 = 底 * 高 / 2)
def triangle_area(b,h):
    """
    根据三角形的底和高, 计算三角形的面积
    :param b: 底
    :param h: 高
    :return: 三角形的面积
    """
    return round(b * h / 2, 1)

triangle_area = triangle_area(5,5)
print(triangle_area)

# 需求2: 计算传入的字符串中元音字母的个数 (元音字母为 aeiouAEIOU)
def vowel_num(s):
    """
    计算传入的字符串中元音字母的个数
    :param s: 传入的字符串
    :return: 字符串中元音字母的个数
    """
    n = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in s.lower():
      if v in vowels:
          n += 1
    return n
s1 = input("请传入字符串: ")
print(vowel_num(s1))

# 案例3：定义一个函数: 计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
def calc_score(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param score_list: 分数列表
    :return: 最高分，最低分，平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg_s

s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
max_score, min_score, avg_score = calc_score(s_list)
print("最高分: ", max_score)
print("最低分: ", min_score)
print("平均分: ", avg_score)


# 练习:
# 1.定义一个函数，根据传入的分数，计算对应的分数等级并返回。
#  ・分数 >= 90: A
#  ・分数 >= 75: B
#  ・分数 >= 60: C
#  ・分数 < 60: D
def score(s):
    """
    根据传入的分数，计算对应的分数等级
    :param s: 传入的成绩
    :return: 分数等级
    """
    if s >=90:
        return "A"
    elif s >=75:
        return "B"
    elif s >=60:
        return "C"
    else:
        return "D"
s = int (input("请输入您的分数: "))
print(score(s))

# 2.定义一个函数，用于判断一个字符串是否是回文串，返回 bool 值。
# 把字符串反转，如果和原字符串相同，就是回文串。（如: "level", "radar", "黄山落叶松叶落山黄"）
def is_palindrome(s):
    """
    判断一个字符串是否是回文串
    :param s: 输入的字符串
    :return: True / False
    """
    if s == s[::-1]:
        return "True"
    else:
        return "False"
# 3.定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def sec_to_hms(total_sec):
    """
    将传入的秒转换为小时、分钟、秒
    :param total_sec: 传入的时间
    :return: 小时, 分钟, 秒
    """
    h = total_sec // 3600
    m = (total_sec % 3600) // 60
    s = total_sec % 60
    return h,m,s
time = int(input("请输入以秒为单位的时间: "))
h,m,s = sec_to_hms(time)
print(f"{time}秒等于: {h}小时 {m}分钟 {s}秒")
# 4.定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
def tri_type(a,b,c):
    """
    根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）
    :param a: 第一条边长
    :param b: 第二条边长
    :param c: 第三条边长
    :return: 三角形类型
    """
    # 三角构成条件：任意两边之和大于第三边
    if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        if a==b==c:
            return "等边三角形"
        elif a==b or b==c or a==c:
            return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不能构成三角形"
nums = input("请输入三角形边长(逗号隔开)：").split(",")
a = float(nums[0])
b = float(nums[1])
c = float(nums[2])
print(tri_type(a,b,c))