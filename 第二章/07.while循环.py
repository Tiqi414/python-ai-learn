# while循环:
# i = int (input("请输入一个10以内的整数: "))
# while i <10:
#     print("人生苦短, 我用Python~ ")
#     i +=1
# else:
#     print("执行完毕!")


# 案例: 计算1-100之间所有偶数的累加之和
total = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    # else:
    #     pass
    i += 1
print(f"1-100之间所有偶数的累加之和为: {total}")



