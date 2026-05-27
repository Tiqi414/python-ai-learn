# 案例1: 根据输入的用户名 密码执行登录操作
# 关键字:
#     brake: 只能出现在循环中, 表示结束,跳出循环的含义 (break跳出循环时, while后面的else中的代码将不会执行)
#     continue: 只能出现在循环中, 表示中断本次循环,直接进入下一次循环
num = 0
while True:
    username = input("请输入您的用户名: ")
    password = input("请输入您的密码: ")

    if username == "" or password == "":
        print("输入的用户名和密码不能为空! 请重新输入")
        num += 1
        continue    # 结束当前循环, 进入下一次循环

    if username == "admin" and password == "666888":
        print("登录成功")
        break
    elif username == "root" and password == "547527":
        print("登录成功")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功")
        break
    else:
        print("用户名或者密码错误, 请重新输入!")
    num += 1
    if num == 5:
        print("输入错误超过五次, 不允许再操作!")
        break













