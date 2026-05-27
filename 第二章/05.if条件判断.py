# # if条件判断
# score = 700
# if score >680:
#     print("欢迎你来清华读书")
#     print("也恭喜你即将踏入精彩的大学生活!")
#
# print("--------------------------")
#
# # 案例:
# ok_account = "18888888888"
# ok_password = "666888"
#
# account = input("请输入您的账号: ")
# password = input("请输入您的密码: ")
#
# if account == ok_account and password == ok_password:
#     print(f"账号密码正确,欢迎{account}登录!")
#
# else:
#     print("账号或密码错误,请重试")

# # 案例:
# year = int(input("请输入年份: "))
# if year % 100 != 0:
#     if year % 4 == 0:
#         print(f"{year}年份是闰年")
#     else:
#         print(f"{year}不是闰年")
# else:
#     if year % 400 == 0:
#         print(f"{year}年份是闰年")
#     else:
#         print(f"{year}不是闰年")

# year = int(input("请输入年份: "))
# if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
#     print(f"{year}年份是闰年")
# else:
#      print(f"{year}不是闰年")

# 练习
# num = int (input("请输入数字: "))
# if num % 2 ==0:
#     print(f"{num}为偶数")
# else:
#     print(f"{num}为奇数")


# age = int (input("请输入年龄: "))
# if age >= 18:
#     print(f"该用户{age}岁, 已经成年")
# else:
#     print(f"该用户{age}岁, 还未成年")

# num = int (input("请输入数字: "))
# if num != 0:
#     if num > 0:
#         print(f"{num}为正数")
#     else:
#         print(f"{num}为负数")
# else:
#     print(f"{num}既不属于负数,也不属于正数")
# num = int(input("请输入数字："))

# if...elif...else
# num = int (input("请输入数字: "))
# if num > 0:
#     print(f"{num}为正数")
# elif num < 0:
#     print(f"{num}为负数")
# else:


# 案例:
# username = input("请输入用户名: ")
# password = input("请输入密码: ")
#
# if username == "admin" and password == "666888":
#     print("登录成功")
# elif username == "root" and password == "547527":
#     print("登录成功")
# elif username == "zhangsan" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败,用户名或密码错误")




# 练习
# score = float (input("请输入考试成绩: "))
# if score <0 or score >100:
#     print("输入成绩无效,请输入正确的成绩")
# elif score >= 85:
#     print(f"{score}为优秀成绩")
# elif score < 60:
#     print(f"{score}成绩不合格")
# else:
#     print(f"{score}为及格成绩")

"""
amount = float (input("请输入商品总额: "))
if amount < 0:
    print("输入金额无效, 请输入正确的金额")
elif amount >= 500:
    print(f"您本次实际应付金额为: {amount * 0.8:.2f}")
elif amount >= 300:
    print(f"您本次实际应付金额为: {amount * 0.9:.2f}")
elif amount >= 100:
    print(f"您本次实际应付金额为: {amount * 0.95:.2f} ")
else:
    print(f"您本次实际应付金额为: {amount:.2f} ")
"""

# 案例: 三角形类型的判断, 根据输入的三个边的边长(正整数), 判定是等边三角形 等腰三角形 普通三角形, 还是不构成三角形
# pass是一个空语句, 起到一个语法占位的作用

side_a = int (input("请输入三角形的第一条边长: "))
side_b = int (input("请输入三角形的第二条边长: "))
side_c = int (input("请输入三角形的第三条边长: "))
if side_a > 0 and side_b > 0 and side_c > 0:
    if side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b:
        if side_a == side_b == side_c:
            print(f"{side_a} {side_b} {side_c}这三条边长组成的三角形为等边三角形")
        elif side_a ==side_b or side_b == side_c or side_a == side_c:
            print(f"{side_a} {side_b} {side_c}这三条边长组成的三角形为等腰三角形")
        else:
            print(f"{side_a} {side_b} {side_c}这三条边长组成的三角形为普通三角形")
    else:
        print(f"{side_a} {side_b} {side_c}这三条边长不构成三角形!")
else:
    print("请输入正确的边长!")


# 练习
# num = float (input("请输入您的年用电度数: "))
# if num >= 0:
#     if num < 2880:
#         print(f"您的年度用费为: {num * 0.4883}")
#     elif 2880 <= num <= 4800:
#         print(f"您的年度用费为: {2880 *0.4883 + (num -2880) * 0.5883}")
#     else:
#         print(f"您的年度用费为: {2880 *0.4883 + 1920 * 0.5883 + (num - 4800) * 0.7883}")
# else:
#     print("请输入正确的用电度数!")



















