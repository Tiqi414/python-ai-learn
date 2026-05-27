# 猜数字游戏:
# import random
# random_number = random.randint(1, 100)
#
# number = int (input("请输入一个1-100之间的数字: "))
# while True:
#     if random_number == number:
#         break
#     elif random_number > number:
#         print("猜小啦!")
#     elif random_number < number:
#         print("猜大啦!")
#     number = int(input("请继续输入猜的数字: "))
# print(f"恭喜你成功猜对! 随机数是: {random_number}")

# 将1-1000之间(含1000)所有5的倍数的数字累加起来
total = 0
for i in range(1,1001):
    if i % 5 == 0:
        total += i
print(f"1-1000之间5倍数的累加和为: {total}")




