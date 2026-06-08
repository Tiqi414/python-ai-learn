# 案例1: N的阶乘: 定义一个函数, 根据传入的数字, 计算数字阶乘的结果
# def fac(n):
#     """
#     定义一个函数, 根据传入的数字, 计算数字阶乘的结果
#     :param n: 输入的数字
#     :return: 输入数字的阶乘
#     """
#     s = 1
#     if n == 0:
#         return 1
#     else:
#         for i in range(1,n+1):
#             s *= i
#     return s
# num = int (input("请输入需要计算的数字: "))
# print(f"{num}的阶乘为: {fac(num)}")

# 递归调用: 指的是在函数中自己调用自己的情况 ---> 一定得有终结点
def fac(n):
    """
    根据传入的数字, 计算数字阶乘的结果
    fac (n) = fac (n-1) ...
    :param n: 输入的数字
    :return: 输入数字的阶乘
    """
    if n==0:
        return 1
    else:
        return n*fac(n-1)
num = int (input("请输入要传入的数字: "))
print(fac(num))


"""案例2: 电商订单计算器 
    定义一个函数, 用于根据传入的一批商品信息 (商品名 价格 数量), 优惠 (优惠券 积分抵扣), 运费信息计算订单的总金额.
    具体规则如下:
        优惠券需要商品金额满5000才可以使用, 且优惠券金额不能超过商品总价.
        积分抵扣需要商品金额满5000才可以使用, 100积分抵扣1元 (且抵扣金额不得超过商品总价,积分只能整百抵扣) 
"""
def amount(*args, coupon=0, points=0, fre=0.0):
    """
    根据传入的一批商品信息 (商品名 价格 数量), 优惠 (优惠券 积分抵扣), 运费信息计算订单的总金额
    :param args: 商品信息 (商品名 价格 数量) ---> 如: ("鼠标", 188, 2) ("键盘", 388, 1)
    :param coupon: 优惠券
    :param points: 积分
    :param fre: 运费
    :return: 订单的总金额
    """
    # 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    # 1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    # 2.扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    # 3.积分抵扣
    if total_cost >= 5000 and points // 100 <=total_cost:
        total_cost -= points // 100
    # 4.增加运费
    total_cost += fre

    return total_cost
# 测试
total1 = amount(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 3999,1), coupon=10, points=400, fre=9.9)
print(total1)

total2 = amount(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999,1), coupon=10, points=400, fre=9.9)
print(total2)
total3 = amount(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999,1))
print(total3)
