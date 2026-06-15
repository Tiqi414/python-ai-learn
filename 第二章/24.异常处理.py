# 异常处理
# try:
#     print("==============================")
#     print(my_name)
#     print("==============================")
# except NameError as e:
#     print(f"程序运行出错了, 请联系管理员 ~ \n异常信息: {e}")


# try:
#     print("==============================")
#     # print(my_name)
#     # print(1 / 0)
#     # print("ABC"[100])
#     print("ABC".hello)
#     print("==============================")
# except NameError as e:
#     print(f"名字不存在, 请检查变量或者函数名字 \n异常信息: {e}")
# except ZeroDivisionError as e:
#     print(f"0不能做除数 \n异常信息: {e}")
# except IndexError as e:
#     print(f"索引错误 \n异常信息: {e}")
# except Exception as e:
#     print(f"程序运行出错了, 请联系管理员 \n异常信息: {e}")
# finally: # 无论程序是否正常运行, finally代码块中的代码都会执行
#     print("释放资源 ~")


# 异常的传递
def fun1():
    print("fun1 ... running ...")
    fun2()

def fun2():
    print("fun2 ... running ...")
    fun3()

def fun3():
    print("fun3 ... running ...")
    print(my_color)

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print(f"程序出错了, 请联系管理员 \n异常信息: {e}")
