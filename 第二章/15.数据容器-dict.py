# 字典 -- key不能重复 (如果重复, 后面的值, 会覆盖前面的值), key 必须是不可变类型
# 定义字典
# dict1 = {"王林": 670, "李慕婉": 608, "许立国": 580, "韩立": 688}
# print(dict1)
# print(type(dict1))
#
# # 访问
# print(dict1["李慕婉"])
# # 获取
# dict1["李慕婉"] = 688
# print(dict1)


# ------------------------------字典 常见操作-------------------------------
# dict1 = {"王林":670, "李暮婉":608, "许立国":580, "韩立":688}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["涛哥"] = 550
# print(dict1)
#
# # 修改 - key存在就是修改
# dict1["涛哥"] = 620
# print(dict1)
#
# # 查询
# print(dict1["涛哥"])  # 根据key获取value
# print(dict1.get("涛哥"))  # 根据key获取value
#
# print(dict1.keys())  # 获取所有的key
# print(dict1.values()) # 获取所有的value
# print(dict1.items()) # 获取所有的键值对 key:value
#
# # 删除
# score = dict1.pop("许立国")
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
#
# # 遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]}: {item[1]}")


# 案例: 开发一个购物车管理系统,实现商品信息的添加 修改 删除 查询功能. 系统使用字典结构存储商品数据, 通过控制台菜单与用户交互. 具体功能如下:

#  第一次完成, 循环一开始选择错误, 嵌套 while 里面用了 break, 数量和价格数据类型未标注,
#  添加,修改,删除,查询未进行商品判定, 无法确定商品有无, 查询功能为实现, 未使用解包, 直接进行下标查询, 代码运行错误.

# 1.添加购物车: 用户根据提示录入商品名称 以及该商品的价格 数量 保存该商品信息的购物车.
all_dict = {}
while True:
    print("欢迎使用购物车管理系统!")
    print()
    print("================购物车系统==================")
    print("#             1. 添加购物车                #")
    print("#             2. 修改购物车                #")
    print("#             3. 删除购物车                #")
    print("#             4. 查询购物车                #")
    print("#             5. 退出购物车                #")
    print("================购物车系统==================")
    print()
    function = input("请输入您要使用的功能(1-5): ")
    while function == "1":
        name = input ("请输入商品名称: ")
        price = float (input ("请输入商品价格: "))
        s = int (input ("请输入商品数量: "))
        all_dict[name] = (price,s)
        print(f"商品{name}添加购物车成功! ")

        if input("是否继续添加(选择 '是' 或者 '否'): ") == "否":
            break

# 2.修改购物车: 要求用户输入要改的购物车商品名称, 然后再提示输入该商品的价格 数量, 输入完成后修改该商品的信息.
    while function == "2":
        name = input("请输入要修改的购物车商品名称: ")
        if name in all_dict:
            price = float (input("请输入要修改的商品价格: "))
            s = int( input("请输入要修改商品数量: "))
            all_dict[name] =( price,s)
            print(f"商品{name}修改成功!")
        else:
            print("该商品不存在! ")
        if input("是否继续修改(选择 '是' 或者 '否'): ") == "否":
            break

# 3.删除购物车: 要求用户输入要删除的购物车名称, 根据名称删除购物车中的商品.
    while function == "3":
        name = input("请输入购物车中要删除的商品: ")
        ps = all_dict.pop(name)
        if name in all_dict:
            print(f"商品{name}已删除! 价格,数量分别为: {all_dict[name]}")
        else:
            print("该商品不存在!")
        if input("是否继续删除(选择 '是' 或者 '否'): ") == "否":
            break

# 4.查询购物车: 将购物车中的商品信息展示出来, 格式为: "商品名称: xxx, 商品价格: xxx, 商品数量: xxx".
    while function == "4":
        if len(all_dict) == 0:
            print("购物车为空!")
        else:
            print("购物车清单如下: ")
            for key, value in all_dict.items():
                p,s = value
                print(f"商品名称: {key}, 商品价格: {p}, 商品数量: {s}")
        break
# 5.退出购物车
    if function == "5":
        break
print("欢迎下次使用!")


# # 课堂中的实现方式:
# shopping_cart = {}
# menu = """
# ########## 购物车系统 ##########
# #        1. 添加购物车        #
# #        2. 修改购物车        #
# #        3. 删除购物车        #
# #        4. 查询购物车        #
# #        5. 退出购物车        #
# ##############################
# """
# print("欢迎使用购物车管理系统~")
# while True:
#     # 1. 制作菜单
#     print(menu)
#
#     # 2. 执行的具体操作
#     choice = input("请选择要执行的操作(1-5): ")
#     match choice:
#         case "1":  # 添加购物车
#             goods_name = input("输入商品名称: ")
#             goods_price = float(input("输入商品价格: "))
#             goods_num = int(input("请输入商品数量: "))
#
#             # 如果商品存在，则不执行添加，提示信息
#             if goods_name in shopping_cart:
#                 print("该商品已存在，请重新选择 ~")
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("商品添加完毕 ~")
#         case "2":  # 修改购物车
#             goods_name = input("输入要修改的商品名称: ")
#             # 如果商品不存在，则提示错误信息，重新选择
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，请重新选择 ~")
#                 continue
#
#             goods_price = float(input("请输入商品最新的价格: "))
#             goods_num = int(input("请输入商品最新的数量: "))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品修改完毕 ~")
#         case "3":  # 删除购物车
#             goods_name = input("请输入要删除的商品名称: ")
#             # 如果商品不存在，则提示错误信息，重新选择
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，请重新选择 ~")
#             else:
#                 del shopping_cart[goods_name]
#                 print("商品删除完毕 ~")
#
#         case "4":  # 查询购物车
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称: {goods_name}, 商品价格: {goods_info['price']}, 商品数量: {goods_info['num']}")
#
#         case "5":  # 退出购物车
#             print("Bye ~")
#             break