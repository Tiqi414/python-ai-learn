# 字符串 基本操作 ---> 不可变的(无法修改)
# s = "Hello-Python"
#
# print(s[4])
# print(s[-8])
#
# for i in s:
#     print(i)
#
# # 切片
# print(s[0:5])
#
# print(s[6:])
#
# # 反转
# print(s[::-1])


# -------------------------------字符串常用方法-------------------------------
# s = "   Hello-Python-Hello-World        "
#
# # find() 查找指定字符串第一次出现的索引位置
# index = s.index("-")
# print(index)
#
# # count() 统计子字符串在指定字符串中出现的字数
# c = s.count("o")
# print(c)
#
# # upper() 转为大写
# u = s.upper()
# print(u)
#
# # lower() 转为小写
# l = s.lower()
# print(l)
#
# # split() 将字符串按照指定字符串切割 - 列表
# sp = s.split("-")
# print(sp)
#
# # strip() 去除字符串两端的空格
# st = s.split()
# print(st)
#
# # replace() 将字符串中的指定子串替换为新的内容
# r = s.replace("-","_")
# print(r)
#
# # startswith() / endswith 判断字符串是否是以指定字符串开头 / 结尾, 返回布尔值
# sw = s.startswith("Hell")
# print(sw)
# ew = s.endswith("Python")
# print(ew)


# 案例1: 邮箱格式验证
# 方式一:
# while True:
#     s = input("请输入您的邮箱: ")
#     if s.count("@") == 1 and s.count(".") >= 1 :
#         print("邮箱格式正确")
#         break
#     else:
#         print("邮箱格式错误")

# 方式二:
# while True:
#     s = input("请输入您的邮箱: ")
#     if "." in s and s.count("@") == 1:
#         print("邮箱格式正确")
#         break
#     else:
#         print("邮箱格式错误")


# 练习1: 输入一个字符串, 判断字符串是否是回文(两边对称)
# s0 = input("请输入字符串: ")
#
# if s0[::-1] == s0:
#     print("该字符串回文")
# else:
#     print("该字符串不回文")

# 练习2: 将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表内容, 遍历输出出来
s_list = []
for i in range(10):
    s = input(f"请输入第{i+1}个字符串: ")[::-1].upper()
    s_list.append(s)
for s in s_list:
    print(f"反转后的字符串列表为: {s}")







