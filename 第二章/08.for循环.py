# for循环, 遍历输入的字符串

# msg = input("请输入需要遍历的元素: ")
#
# for s in msg: # s 表示遍历出来的元素, msg 表示需要遍历的数据
#     print(f"元素: {s}")
# print("遍历结束!")

# 案例: 计算1-100之间所有奇数之和
# total = 0
# msg = range(1,101,2)
# for i in msg:
#     total += i
# print(f"1-100之间所有奇数和为: {total}")
# 案例: 计算100 -500之间所有三倍数的数字之和
# total = 0
# for i in range(102,501,3):
#     total += i
# print(f"100- 500之间所有三倍数的数字之和为: {total}")


# 循环嵌套: 根据输入的长方形的长度m, 宽度n, 打印一个长方形

# m = int (input("请输入长方形的长度: m = "))
# n = int (input("请输入长方形的宽度: n = "))
#
# for s in range(n):
#     for i in range(m):
#         print(" * " ,end="")
#     print()



# 案例: 打印九九乘法表
# m,n= 9,1
# for s in range(m):
#     for i in range(1,n + 1):
#         print(f"{i} x {n} = {i * n}", end="  ")
#     n += 1
#     print()


# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(f"{j} x {i} = {j * i}",end="\t")
#     print()


# 练习
# 根据输入的直角形边长, 打印等腰直角三角形
# n = int (input("请输入直角边的边长: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="\t")
#     print()

# 根据输入的数字, 打印对应的数字金字塔
# m = int (input("请输入数字: "))
# for s in range(1,m + 1):
#     for t in range(1,s +1):
#         print(f"{t}",end="\t")
#     print ()

# 打印国际象棋棋盘
# 第一次尝试写
# for i in range(4):
#     for j in range(8):
#         if j%2 == 0:
#             print(" ■ ", end="")
#         else:
#             print(" □ ", end="")
#     print()
#     for t in range(8):
#         if t%2 == 1:
#             print(" ■ ", end="")
#         else:
#             print(" □ ", end="")
#     print()

# 第二次:
for i in range(8):
    for j in range(8):
        if (i + j)%2 == 0:
            print(" ■ ", end="")
        else:
            print(" □ ", end="")
    print()








